#!/usr/bin/env python3
import uuid
import json
import urllib.request
import urllib.error
import os

TALLY_API_KEY = os.environ.get("TALLY_API_KEY", "YOUR_TALLY_API_KEY")
TALLY_API_URL = "https://api.tally.so/forms"


def uid():
    return str(uuid.uuid4())


def form_title(title):
    gid = uid()
    return [
        {
            "uuid": uid(),
            "type": "FORM_TITLE",
            "groupUuid": gid,
            "groupType": "FORM_TITLE",
            "payload": {"html": title},
        }
    ]


def page_break():
    gid = uid()
    return [
        {
            "uuid": uid(),
            "type": "PAGE_BREAK",
            "groupUuid": gid,
            "groupType": "PAGE_BREAK",
            "payload": {},
        }
    ]


def heading(text, level=2):
    t = f"HEADING_{level}"
    gid = uid()
    return [
        {
            "uuid": uid(),
            "type": t,
            "groupUuid": gid,
            "groupType": t,
            "payload": {"html": text},
        }
    ]


def desc(text):
    gid = uid()
    return [
        {
            "uuid": uid(),
            "type": "TEXT",
            "groupUuid": gid,
            "groupType": "TEXT",
            "payload": {"html": text},
        }
    ]


def text_q(label, input_type="INPUT_TEXT", required=False, placeholder=""):
    title_gid = uid()
    input_gid = uid()
    payload_input = {}
    if required:
        payload_input["isRequired"] = True
    if placeholder:
        payload_input["placeholder"] = placeholder
    return [
        {
            "uuid": uid(),
            "type": "TITLE",
            "groupUuid": title_gid,
            "groupType": "QUESTION",
            "payload": {"html": label},
        },
        {
            "uuid": uid(),
            "type": input_type,
            "groupUuid": input_gid,
            "groupType": input_type,
            "payload": payload_input,
        },
    ]


def dropdown_q(label, options):
    title_gid = uid()
    opts_gid = uid()
    blocks = [
        {
            "uuid": uid(),
            "type": "TITLE",
            "groupUuid": title_gid,
            "groupType": "QUESTION",
            "payload": {"html": label},
        },
    ]
    last_idx = len(options) - 1
    for i, opt in enumerate(options):
        blocks.append(
            {
                "uuid": uid(),
                "type": "DROPDOWN_OPTION",
                "groupUuid": opts_gid,
                "groupType": "DROPDOWN",
                "payload": {
                    "index": i,
                    "text": opt,
                    "isFirst": i == 0,
                    "isLast": i == last_idx,
                },
            }
        )
    return blocks


def mc_q(label, options):
    title_gid = uid()
    opts_gid = uid()
    blocks = [
        {
            "uuid": uid(),
            "type": "TITLE",
            "groupUuid": title_gid,
            "groupType": "QUESTION",
            "payload": {"html": label},
        },
    ]
    last_idx = len(options) - 1
    for i, opt in enumerate(options):
        blocks.append(
            {
                "uuid": uid(),
                "type": "MULTIPLE_CHOICE_OPTION",
                "groupUuid": opts_gid,
                "groupType": "MULTIPLE_CHOICE",
                "payload": {
                    "index": i,
                    "text": opt,
                    "isFirst": i == 0,
                    "isLast": i == last_idx,
                },
            }
        )
    return blocks


def cb_q(label, options):
    title_gid = uid()
    opts_gid = uid()
    blocks = [
        {
            "uuid": uid(),
            "type": "TITLE",
            "groupUuid": title_gid,
            "groupType": "QUESTION",
            "payload": {"html": label},
        },
    ]
    last_idx = len(options) - 1
    for i, opt in enumerate(options):
        blocks.append(
            {
                "uuid": uid(),
                "type": "CHECKBOX",
                "groupUuid": opts_gid,
                "groupType": "CHECKBOXES",
                "payload": {
                    "index": i,
                    "text": opt,
                    "isFirst": i == 0,
                    "isLast": i == last_idx,
                },
            }
        )
    return blocks


def file_q(label):
    title_gid = uid()
    file_gid = uid()
    return [
        {
            "uuid": uid(),
            "type": "TITLE",
            "groupUuid": title_gid,
            "groupType": "QUESTION",
            "payload": {"html": label},
        },
        {
            "uuid": uid(),
            "type": "FILE_UPLOAD",
            "groupUuid": file_gid,
            "groupType": "FILE_UPLOAD",
            "payload": {},
        },
    ]


# ━━━ BUILD FORM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
blocks = []

# ━━━ FORM TITLE ━━━
blocks += form_title("แบบสอบถามข้อมูลสำหรับสร้างเว็บไซต์ — Website Project Brief")

# ━━━ PAGE 1: ข้อมูลธุรกิจ ━━━
blocks += heading("📋 ข้อมูลธุรกิจ (Business Information)")
blocks += desc("<em>กรุณากรอกข้อมูลพื้นฐานของธุรกิจ</em>")

blocks += text_q(
    "ชื่อธุรกิจ / ร้าน / คลินิก *", "INPUT_TEXT", True, "เช่น คลินิกรักสัตว์, ร้านกาแฟบ้านสวน"
)

blocks += dropdown_q(
    "ประเภทธุรกิจ *",
    [
        "คลินิกสัตว์ / โรงพยาบาลสัตว์ (Vet Clinic)",
        "ร้านอาหาร / คาเฟ่ (Restaurant / Cafe)",
        "ร้านเสริมสวย / สปา (Beauty Salon / Spa)",
        "ฟิตเนส / โยคะ / ยิม (Fitness / Gym)",
        "โรงแรม / ที่พัก (Hotel / Accommodation)",
        "ร้านค้า / ขายสินค้า (Retail / Shop)",
        "บริการทั่วไป (General Services)",
        "อื่นๆ (Other)",
    ],
)

blocks += text_q("ชื่อเจ้าของ / ผู้ดูแลหลัก *", "INPUT_TEXT", True, "ชื่อ-นามสกุล")
blocks += text_q("ตำแหน่ง / คุณวุฒิ", "INPUT_TEXT", False, "เช่น สพ.ญ., เชฟ, เจ้าของร้าน")
blocks += text_q("ที่อยู่ธุรกิจ *", "TEXTAREA", True, "ที่อยู่เต็ม เพื่อใช้แสดงบน Google Maps")
blocks += text_q("เบอร์โทรศัพท์ *", "INPUT_PHONE_NUMBER", True)
blocks += text_q("อีเมล *", "INPUT_EMAIL", True, "email@example.com")
blocks += text_q("LINE ID", "INPUT_TEXT", False, "@lineid หรือ ชื่อ LINE")
blocks += text_q("เวลาทำการ *", "INPUT_TEXT", True, "เช่น จ-ศ 9:00-18:00, ส 9:00-12:00")

# ━━━ PAGE 2: ช่องทางออนไลน์ ━━━
blocks += page_break()
blocks += heading("🌐 ช่องทางออนไลน์ (Online Presence)")
blocks += desc("<em>เราจะดึงข้อมูลและรูปภาพจากโซเชียลมีเดียเพื่อใช้สร้างเว็บไซต์</em>")

blocks += text_q(
    "Facebook Page URL *", "INPUT_LINK", True, "https://facebook.com/YourPage"
)
blocks += text_q(
    "Instagram URL", "INPUT_LINK", False, "https://instagram.com/yourbusiness"
)
blocks += text_q("TikTok URL", "INPUT_LINK", False, "https://tiktok.com/@yourbusiness")
blocks += text_q(
    "Google Maps ลิงก์", "INPUT_LINK", False, "ค้นหาร้านใน Google Maps แล้วกดแชร์ลิงก์"
)
blocks += text_q("เว็บไซต์ปัจจุบัน (ถ้ามี)", "INPUT_LINK", False, "https://yourbusiness.com")
blocks += text_q("ช่องทางอื่นๆ", "TEXTAREA", False, "YouTube, LINE OA, หรือช่องทางอื่นๆ")

# ━━━ PAGE 3: แบรนด์และภาพลักษณ์ ━━━
blocks += page_break()
blocks += heading("🎨 แบรนด์และภาพลักษณ์ (Branding)")

blocks += file_q("โลโก้ธุรกิจ (Business Logo)")
blocks += desc("รองรับ PNG, SVG, PDF — ถ้ายังไม่มี เราช่วยออกแบบให้ได้")

blocks += mc_q(
    "มีสีประจำแบรนด์ไหม? *",
    [
        "มี (Yes)",
        "ไม่มี / ยังไม่แน่ใจ (No / Not sure)",
    ],
)

blocks += text_q(
    "สีประจำแบรนด์ (ถ้ามี)", "INPUT_TEXT", False, "ระบุสี เช่น น้ำเงินเข้ม, ทอง หรือรหัสสี #003366"
)

blocks += mc_q(
    "มีรูปถ่ายมืออาชีพพร้อมใช้ไหม? *",
    [
        "มี — มีรูปถ่ายมืออาชีพพร้อมใช้งาน",
        "มีบ้าง — มีรูปบางส่วน ใช้รูปจาก Facebook เพิ่มได้",
        "ยังไม่มี — ใช้รูปจาก Facebook ไปก่อน",
    ],
)

blocks += file_q("อัปโหลดรูปถ่าย (ถ้ามี)")
blocks += desc("รูปถ่ายธุรกิจ, สินค้า, ทีมงาน — อัปโหลดได้หลายไฟล์")
blocks += file_q("Brand guideline / Style guide (ถ้ามี)")

# ━━━ PAGE 4: บริการและเนื้อหา ━━━
blocks += page_break()
blocks += heading("📝 บริการและเนื้อหา (Services & Content)")

blocks += text_q(
    "บริการ/สินค้าหลักของคุณ *", "TEXTAREA", True, "ลิสต์บริการหรือสินค้าหลักทั้งหมด พร้อมรายละเอียดสั้นๆ"
)
blocks += text_q("จุดเด่นของธุรกิจ *", "TEXTAREA", True, "อะไรที่ทำให้ธุรกิจคุณแตกต่างจากคู่แข่ง?")

blocks += mc_q(
    "ต้องการแสดงราคาบนเว็บไซต์ไหม? *",
    [
        "แสดงราคาเต็ม (Show full pricing)",
        "แสดงช่วงราคา เช่น เริ่มต้น xxx บาท (Price ranges)",
        "ไม่แสดง — ให้ติดต่อสอบถาม (Don't show)",
    ],
)

blocks += text_q(
    "รายการราคา (ถ้าต้องการแสดง)", "TEXTAREA", False, "พิมพ์รายการราคา หรืออัปโหลดไฟล์ในข้อถัดไป"
)
blocks += file_q("อัปโหลดไฟล์ราคา (ถ้ามี)")
blocks += text_q(
    "ทีมงาน / บุคลากรที่อยากแนะนำ", "TEXTAREA", False, "ชื่อ, ตำแหน่ง, ความเชี่ยวชาญ ของแต่ละคน"
)
blocks += text_q(
    "รีวิว / คำชื่นชมจากลูกค้า",
    "TEXTAREA",
    False,
    "คัดลอกรีวิวดีๆ จากลูกค้า 3-5 รายการ (พร้อมชื่อผู้รีวิว)",
)
blocks += text_q(
    "ประเภทสินค้า/บริการที่รับ",
    "TEXTAREA",
    False,
    "เช่น สัตว์เลี้ยงประเภทที่รับรักษา, ประเภทอาหารที่ขาย ฯลฯ",
)

blocks += heading("📋 ข้อมูลที่จะช่วยให้เว็บไซต์สมบูรณ์ยิ่งขึ้น", 3)
blocks += desc(
    "<em>ไม่ต้องเตรียมตอนนี้ — หลังส่งแบบฟอร์มแล้ว เราจะส่งรายการข้อมูลที่แนะนำให้เตรียมตามประเภทธุรกิจของคุณ</em>"
)
blocks += desc("• ตารางราคาบริการ / เมนู")
blocks += desc("• ข้อมูลทีมงาน (ชื่อ, ความเชี่ยวชาญ, ตารางทำงาน)")
blocks += desc("• คำถามที่ลูกค้าถามบ่อย (FAQ)")
blocks += desc("• รูปถ่ายสถานที่ / สินค้า / ผลงาน")

# ━━━ PAGE 5: ความต้องการเว็บไซต์ ━━━
blocks += page_break()
blocks += heading("🎯 ความต้องการเว็บไซต์ (Website Preferences)")

blocks += dropdown_q(
    "เป้าหมายหลักของเว็บไซต์คืออะไร? *",
    [
        "ให้ลูกค้าใหม่หาเจอและติดต่อมา (Get new customers)",
        "สร้างความน่าเชื่อถือให้ธุรกิจ (Build trust & credibility)",
        "แสดงบริการและผลงาน (Showcase services & portfolio)",
        "ให้ข้อมูลและตอบคำถามที่พบบ่อย (Provide info & FAQs)",
        "รับจองออนไลน์ (Online booking)",
    ],
)

blocks += text_q(
    "กลุ่มลูกค้าเป้าหมาย", "TEXTAREA", False, "ลูกค้าของคุณเป็นใคร? อายุ, พื้นที่, ไลฟ์สไตล์"
)
blocks += text_q(
    "เว็บไซต์ที่ชอบ (แชร์ลิงก์ 1-3 เว็บ)",
    "TEXTAREA",
    False,
    "แชร์ลิงก์เว็บไซต์ที่คุณชอบดีไซน์ เราจะใช้เป็นแรงบันดาลใจ",
)

blocks += mc_q(
    "สไตล์ที่ชอบ *",
    [
        "🌿 อบอุ่น เป็นกันเอง — โทนอ่อน สีพาสเทล มุมโค้งมน",
        "✨ สะอาด ทันสมัย — มินิมอล พื้นที่ว่างเยอะ ดูโปร",
        "💪 โดดเด่น เข้มแข็ง — สีสดใส ตัวอักษรใหญ่ มีพลัง",
        "👑 หรูหรา พรีเมียม — สีเข้ม ทองคำ ดูหรู",
        "🎨 สนุก มีสีสัน — ร่าเริง หลากสี มีชีวิตชีวา",
    ],
)

blocks += mc_q(
    "ภาษาบนเว็บไซต์ *",
    [
        "ไทยอย่างเดียว (Thai only)",
        "ไทย + อังกฤษ (Thai + English bilingual)",
        "อังกฤษอย่างเดียว (English only)",
    ],
)

blocks += mc_q(
    "ปุ่มหลักที่ลูกค้าจะกด (CTA) *",
    [
        "แชท LINE",
        "โทรศัพท์ (Phone call)",
        "WhatsApp",
        "อีเมล (Email)",
        "จองออนไลน์ (Book online)",
        "แผนที่ / นำทาง (Map / Directions)",
    ],
)

blocks += cb_q(
    "ต้องการหน้าอะไรบ้าง? (เลือกได้หลายข้อ) *",
    [
        "หน้าแรก / Home",
        "เกี่ยวกับเรา / About Us",
        "บริการ / Services",
        "ราคา / Pricing",
        "ทีมงาน / Our Team",
        "แกลเลอรี่ผลงาน / Gallery",
        "รีวิวลูกค้า / Testimonials",
        "คำถามที่พบบ่อย / FAQ",
        "ติดต่อเรา / Contact",
        "บล็อก / Blog",
    ],
)

blocks += dropdown_q(
    "จำนวนหน้าเว็บไซต์ที่ต้องการโดยประมาณ *",
    [
        "1-3 หน้า (เว็บไซต์เรียบง่าย)",
        "4-6 หน้า (เว็บไซต์มาตรฐาน)",
        "7-10 หน้า (เว็บไซต์ครบถ้วน)",
        "10+ หน้า (เว็บไซต์ขนาดใหญ่)",
    ],
)

blocks += text_q(
    "ถ้าต้องการหลายหน้า — แต่ละหน้าเกี่ยวกับอะไร?",
    "TEXTAREA",
    False,
    "อธิบายสั้นๆ เช่น หน้าบริการ: รายละเอียดบริการทั้งหมด, หน้าทีมงาน: แนะนำหมอและพนักงาน",
)

# ━━━ PAGE 6: โดเมนและการส่งมอบ ━━━
blocks += page_break()
blocks += heading("🚀 โดเมนและการส่งมอบ (Domain & Delivery)")

blocks += mc_q(
    "มีโดเมน (ชื่อเว็บไซต์) แล้วหรือยัง? *",
    [
        "มีแล้ว (Yes, I have a domain)",
        "ยังไม่มี (No, I need one)",
    ],
)

blocks += text_q("โดเมนของคุณคือ (ถ้ามี)", "INPUT_TEXT", False, "เช่น mybusiness.com")
blocks += text_q(
    "ชื่อโดเมนที่ต้องการ (ถ้ายังไม่มี)",
    "INPUT_TEXT",
    False,
    "เช่น mybusiness.com — เราจะช่วยเช็คว่าว่างไหม",
)

blocks += mc_q(
    "ต้องการอีเมลธุรกิจไหม? (เช่น info@yourbusiness.com)",
    [
        "ต้องการ (Yes)",
        "ไม่ต้องการ (No)",
        "ยังไม่แน่ใจ (Not sure)",
    ],
)

blocks += mc_q(
    "ต้องการติดตั้ง Google Analytics ไหม? (ดูสถิติผู้เข้าชมเว็บไซต์)",
    [
        "ต้องการ — อยากดูสถิติผู้เข้าชม",
        "ยังไม่แน่ใจ — ให้ช่วยตัดสินใจ",
        "ไม่ต้องการ",
    ],
)

blocks += mc_q(
    "รูปแบบการส่งมอบที่ต้องการ *",
    [
        "ส่งมอบทั้งหมด (Full Handover) — โอนทุกบัญชีให้คุณดูแลเอง จ่ายครั้งเดียว",
        "ดูแลรายเดือน (Managed Service) — เราดูแลเว็บไซต์ให้ คุณจ่ายค่าดูแลรายเดือน",
    ],
)

# ━━━ PAGE 7: เพิ่มเติม ━━━
blocks += page_break()
blocks += heading("💬 เพิ่มเติม (Additional Notes)")

blocks += text_q(
    "มีอะไรอื่นที่อยากบอกเราไหม?", "TEXTAREA", False, "ความต้องการพิเศษ, ไอเดีย, หรือข้อกังวลใดๆ"
)

blocks += mc_q(
    "ช่องทางติดต่อที่สะดวกที่สุด *",
    [
        "LINE",
        "โทรศัพท์ (Phone)",
        "อีเมล (Email)",
    ],
)

blocks += mc_q(
    "ช่วงเวลาที่สะดวกให้ติดต่อ",
    [
        "เช้า (8:00-12:00)",
        "บ่าย (12:00-17:00)",
        "เย็น (17:00-20:00)",
        "ตลอดเวลา (Anytime)",
    ],
)

blocks += dropdown_q(
    "รู้จักเราจากไหน?",
    [
        "เพื่อนแนะนำ (Referral)",
        "Facebook",
        "Google ค้นหา",
        "Instagram",
        "อื่นๆ (Other)",
    ],
)


# ━━━ SEND TO API ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
payload = {"status": "PUBLISHED", "blocks": blocks, "settings": {"language": "th"}}

print(f"Total blocks: {len(blocks)}")
print("Creating form on Tally.so...")

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    TALLY_API_URL,
    data=data,
    method="POST",
    headers={
        "Authorization": f"Bearer {TALLY_API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "application/json",
    },
)

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        fid = result.get("id", "unknown")
        print(f"\n✅ Form created!")
        print(f"   Form ID:  {fid}")
        print(f"   Name:     {result.get('name')}")
        print(f"   Edit:     https://tally.so/forms/{fid}/edit")
        print(f"   Share:    https://tally.so/r/{fid}")
        print(f"\n{json.dumps(result, indent=2, ensure_ascii=False)}")
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"\n❌ Error {e.code}: {e.reason}")
    print(f"   {body}")
except Exception as e:
    print(f"\n❌ Error: {e}")
