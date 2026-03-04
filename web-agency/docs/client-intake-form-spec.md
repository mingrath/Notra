# Client Intake Form — Complete Spec for Tally.so

> Blueprint for building the client intake form on Tally.so
> This form feeds into the `website-from-scraping` pipeline (Phases 3-4)

## Form Settings

- **Title:** แบบสอบถามข้อมูลสำหรับสร้างเว็บไซต์ | Website Project Brief
- **Language:** Thai primary, English field names in parentheses
- **Completion message:** "ขอบคุณค่ะ! เราจะติดต่อกลับภายใน 24 ชั่วโมง 🎉"
- **Notifications:** Email to mingrath@gmail.com on each submission
- **Webhook (optional):** Google Sheets integration for tracking

---

## Page 1: ข้อมูลธุรกิจ (Business Information)

### Fields:

| # | Label (TH) | Label (EN) | Type | Required | Notes |
|---|-----------|-----------|------|----------|-------|
| 1.1 | ชื่อธุรกิจ / ร้าน / คลินิก | Business Name | Short text | ✅ | |
| 1.2 | ประเภทธุรกิจ | Business Type | Dropdown | ✅ | See options below |
| 1.3 | ชื่อเจ้าของ / ผู้ดูแลหลัก | Owner / Key Person Name | Short text | ✅ | |
| 1.4 | ตำแหน่ง / คุณวุฒิ | Title / Credentials | Short text | ❌ | e.g., "สพ.ญ.", "Chef", "นักกายภาพ" |
| 1.5 | ที่อยู่ธุรกิจ | Business Address | Long text | ✅ | Full address for Google Maps |
| 1.6 | เบอร์โทรศัพท์ | Phone Number | Short text | ✅ | |
| 1.7 | อีเมล | Email | Email | ✅ | |
| 1.8 | LINE ID | LINE ID | Short text | ❌ | |
| 1.9 | เวลาทำการ | Operating Hours | Long text | ✅ | e.g., "จ-ศ 9:00-18:00, ส 9:00-12:00" |

**Dropdown options for 1.2 (Business Type):**
- คลินิกสัตว์ / โรงพยาบาลสัตว์ (Vet Clinic / Animal Hospital)
- ร้านอาหาร / คาเฟ่ (Restaurant / Cafe)
- ร้านเสริมสวย / สปา (Beauty Salon / Spa)
- ฟิตเนส / โยคะ / ยิม (Fitness / Yoga / Gym)
- โรงแรม / ที่พัก (Hotel / Accommodation)
- ร้านค้า / ขายสินค้า (Retail / Shop)
- บริการทั่วไป (General Services)
- อื่นๆ (Other) → Show text field for custom input

---

## Page 2: ช่องทางออนไลน์ (Online Presence)

### Fields:

| # | Label (TH) | Label (EN) | Type | Required | Notes |
|---|-----------|-----------|------|----------|-------|
| 2.1 | Facebook Page URL | Facebook Page | URL | ✅ | ⚠️ ต้องเป็นลิงก์เพจ ไม่ใช่โปรไฟล์ส่วนตัว |
| 2.2 | Instagram URL | Instagram | URL | ❌ | |
| 2.3 | TikTok URL | TikTok | URL | ❌ | |
| 2.4 | Google Maps ลิงก์ | Google Maps Link | URL | ❌ | "ค้นหาร้านใน Google Maps แล้วกดแชร์ลิงก์" |
| 2.5 | เว็บไซต์ปัจจุบัน (ถ้ามี) | Current Website | URL | ❌ | |
| 2.6 | ช่องทางอื่นๆ | Other Channels | Long text | ❌ | YouTube, LINE OA, etc. |

**Helper text for 2.1:**
> "กรุณาใส่ลิงก์ Facebook Page ของธุรกิจ เช่น https://facebook.com/YourBusinessPage
> เราจะดึงข้อมูลและรูปภาพจากเพจเพื่อใช้ในการสร้างเว็บไซต์"

---

## Page 3: แบรนด์และภาพลักษณ์ (Branding & Visual Identity)

### Fields:

| # | Label (TH) | Label (EN) | Type | Required | Notes |
|---|-----------|-----------|------|----------|-------|
| 3.1 | โลโก้ธุรกิจ | Business Logo | File upload | ❌ | Accept: PNG, SVG, PDF, AI. "ถ้ายังไม่มีโลโก้ เราช่วยออกแบบให้ได้" |
| 3.2 | มีสีประจำแบรนด์ไหม? | Do you have brand colors? | Yes/No | ✅ | |
| 3.3 | 🔀 สีประจำแบรนด์ | Brand Colors | Short text | ❌ | **Show IF 3.2 = Yes.** "ระบุสี เช่น น้ำเงินเข้ม, ทอง หรือรหัสสี #003366" |
| 3.4 | รูปถ่ายมืออาชีพ | Professional Photos | Multiple choice | ✅ | See options below |
| 3.5 | 🔀 อัปโหลดรูปถ่าย | Upload Photos | File upload (multiple) | ❌ | **Show IF 3.4 = "มี".** Accept: JPG, PNG. Max 20 files |
| 3.6 | Brand guideline / Style guide (ถ้ามี) | Brand Guide | File upload | ❌ | |

**Options for 3.4 (Professional Photos):**
- มี — มีรูปถ่ายมืออาชีพพร้อมใช้งาน (Yes — have professional photos ready)
- มีบ้าง — มีรูปบางส่วน ใช้รูปจาก Facebook เพิ่มได้ (Some — have some, can supplement from Facebook)
- ยังไม่มี — ใช้รูปจาก Facebook ไปก่อน (No — use Facebook photos for now)

---

## Page 4: บริการและเนื้อหา (Services & Content)

### Fields:

| # | Label (TH) | Label (EN) | Type | Required | Notes |
|---|-----------|-----------|------|----------|-------|
| 4.1 | บริการ/สินค้าหลักของคุณ | Main Services / Products | Long text | ✅ | "ลิสต์บริการหรือสินค้าหลักทั้งหมด พร้อมรายละเอียดสั้นๆ" |
| 4.2 | จุดเด่นของธุรกิจ | What Makes You Special | Long text | ✅ | "อะไรที่ทำให้ธุรกิจคุณแตกต่างจากคู่แข่ง?" |
| 4.3 | ต้องการแสดงราคาบนเว็บไซต์ไหม? | Show Pricing? | Multiple choice | ✅ | See options below |
| 4.4 | 🔀 รายการราคา | Price List | Long text or File upload | ❌ | **Show IF 4.3 = "แสดง"** |
| 4.5 | ทีมงาน / บุคลากรที่อยากแนะนำ | Team Members to Feature | Long text | ❌ | "ชื่อ, ตำแหน่ง, ความเชี่ยวชาญ ของแต่ละคน" |
| 4.6 | รีวิว / คำชื่นชมจากลูกค้า | Customer Testimonials | Long text | ❌ | "คัดลอกรีวิวดีๆ จากลูกค้า 3-5 รายการ" |
| 4.7 | สัตว์เลี้ยง/สินค้าประเภทที่รับ | Types/Categories Handled | Long text | ❌ | Only for relevant businesses |

**Options for 4.3 (Show Pricing):**
- แสดงราคาเต็ม (Show full pricing)
- แสดงช่วงราคา เช่น "เริ่มต้น xxx บาท" (Show price ranges only)
- ไม่แสดง — ให้ติดต่อสอบถาม (Don't show — contact for pricing)

---

## Page 5: ความต้องการเว็บไซต์ (Website Preferences)

### Fields:

| # | Label (TH) | Label (EN) | Type | Required | Notes |
|---|-----------|-----------|------|----------|-------|
| 5.1 | เป้าหมายหลักของเว็บไซต์คืออะไร? | Primary Goal | Dropdown | ✅ | See options below |
| 5.2 | กลุ่มลูกค้าเป้าหมาย | Target Audience | Long text | ❌ | "ลูกค้าของคุณเป็นใคร? อายุ, พื้นที่, ไลฟ์สไตล์" |
| 5.3 | เว็บไซต์ที่ชอบ (ส่งลิงก์ 1-3 เว็บ) | Websites You Like | Long text | ❌ | "แชร์ลิงก์เว็บไซต์ที่คุณชอบดีไซน์ เราจะใช้เป็นแรงบันดาลใจ" |
| 5.4 | สไตล์ที่ชอบ | Preferred Style | Multiple choice | ✅ | See options below |
| 5.5 | ภาษาบนเว็บไซต์ | Website Language | Multiple choice | ✅ | See options below |
| 5.6 | ปุ่มหลักที่ลูกค้าจะกด (CTA) | Primary Call-to-Action | Multiple choice | ✅ | See options below |
| 5.7 | ต้องการหน้าอะไรบ้าง? | Pages Needed | Checkbox (multiple) | ✅ | See options below |

**Dropdown for 5.1 (Primary Goal):**
- ให้ลูกค้าใหม่หาเจอและติดต่อมา (Get new customers to find & contact us)
- สร้างความน่าเชื่อถือให้ธุรกิจ (Build trust & credibility)
- แสดงบริการและผลงาน (Showcase services & portfolio)
- ให้ข้อมูลและตอบคำถามที่พบบ่อย (Provide info & FAQs)
- รับจองออนไลน์ (Online booking)

**Options for 5.4 (Preferred Style):**
- 🌿 อบอุ่น เป็นกันเอง (Warm & Friendly) — โทนอ่อน สีพาสเทล มุมโค้งมน
- ✨ สะอาด ทันสมัย (Clean & Modern) — มินิมอล พื้นที่ว่างเยอะ ดูโปร
- 💪 โดดเด่น เข้มแข็ง (Bold & Energetic) — สีสดใส ตัวอักษรใหญ่ มีพลัง
- 👑 หรูหรา พรีเมียม (Elegant & Premium) — สีเข้ม ทองคำ ดูหรู
- 🎨 สนุก มีสีสัน (Playful & Colorful) — ร่าเริง หลากสี มีชีวิตชีวา

**Options for 5.5 (Language):**
- ไทยอย่างเดียว (Thai only)
- ไทย + อังกฤษ (Thai + English bilingual)
- อังกฤษอย่างเดียว (English only)

**Options for 5.6 (Primary CTA):**
- แชท LINE (Chat via LINE)
- โทรศัพท์ (Phone call)
- WhatsApp
- อีเมล (Email)
- จองออนไลน์ (Book online)
- แผนที่ / นำทาง (Map / Directions)

**Checkbox options for 5.7 (Pages Needed):**
- หน้าแรก / Home (ต้องมี) ✅ always selected
- เกี่ยวกับเรา / About Us
- บริการ / Services
- ราคา / Pricing
- ทีมงาน / Our Team
- แกลเลอรี่ผลงาน / Gallery / Portfolio
- รีวิวลูกค้า / Testimonials
- คำถามที่พบบ่อย / FAQ
- ติดต่อเรา / Contact
- บล็อก / Blog (แนะนำเพิ่มทีหลัง)

---

## Page 6: โดเมนและการส่งมอบ (Domain & Delivery)

### Fields:

| # | Label (TH) | Label (EN) | Type | Required | Notes |
|---|-----------|-----------|------|----------|-------|
| 6.1 | มีโดเมน (ชื่อเว็บไซต์) แล้วหรือยัง? | Do you have a domain? | Yes/No | ✅ | |
| 6.2 | 🔀 โดเมนของคุณคือ | Your Domain | Short text | ❌ | **Show IF 6.1 = Yes.** e.g., "mybusiness.com" |
| 6.3 | 🔀 ชื่อโดเมนที่ต้องการ | Preferred Domain Name | Short text | ❌ | **Show IF 6.1 = No.** "เราจะช่วยเช็คว่าว่างไหมและจดให้" |
| 6.4 | ต้องการอีเมลธุรกิจไหม? | Need Business Email? | Yes/No + description | ✅ | "เช่น info@yourbusiness.com — ดูเป็นมืออาชีพกว่า Gmail" |
| 6.5 | ต้องการติดตั้ง Google Analytics ไหม? | Need Google Analytics? | Multiple choice | ✅ | |
| 6.6 | รูปแบบการส่งมอบที่ต้องการ | Delivery Model | Multiple choice | ✅ | See options below |

**Options for 6.5 (Analytics):**
- ต้องการ — อยากดูสถิติผู้เข้าชม (Yes — want to see visitor stats)
- ยังไม่แน่ใจ — ให้ช่วยตัดสินใจ (Not sure — help me decide)
- ไม่ต้องการ (No)

**Options for 6.6 (Delivery Model):**
- **ส่งมอบทั้งหมด (Full Handover)** — โอนทุกบัญชี (โดเมน, โฮสต์, โค้ด) ให้คุณดูแลเอง จ่ายครั้งเดียว
- **ดูแลรายเดือน (Managed Service)** — เราดูแลเว็บไซต์ให้ คุณจ่ายค่าดูแลรายเดือน พร้อมแก้ไขเนื้อหาให้ฟรี

---

## Page 7: เพิ่มเติม (Additional Notes)

### Fields:

| # | Label (TH) | Label (EN) | Type | Required | Notes |
|---|-----------|-----------|------|----------|-------|
| 7.1 | มีอะไรอื่นที่อยากบอกเราไหม? | Anything else? | Long text | ❌ | |
| 7.2 | ช่องทางติดต่อที่สะดวกที่สุด | Preferred Contact Method | Multiple choice | ✅ | LINE / โทรศัพท์ / อีเมล |
| 7.3 | ช่วงเวลาที่สะดวกให้ติดต่อ | Best Time to Contact | Multiple choice | ❌ | เช้า / บ่าย / เย็น / ตลอดเวลา |
| 7.4 | รู้จักเราจากไหน? | How did you find us? | Dropdown | ❌ | เพื่อนแนะนำ / Facebook / Google / อื่นๆ |

---

## Conditional Logic Summary (Tally.so)

| Condition | Show Field |
|-----------|-----------|
| 3.2 = Yes (มีสีแบรนด์) | → 3.3 (Brand Colors) |
| 3.4 = "มี" (Have photos) | → 3.5 (Upload Photos) |
| 4.3 = "แสดงราคาเต็ม" or "แสดงช่วงราคา" | → 4.4 (Price List) |
| 6.1 = Yes (มีโดเมน) | → 6.2 (Your Domain) |
| 6.1 = No (ยังไม่มีโดเมน) | → 6.3 (Preferred Domain Name) |

---

## Data → Pipeline Mapping

| Form Field | Maps to Pipeline Phase | Used In |
|------------|----------------------|---------|
| 2.1 Facebook URL | Phase 1: SCRAPE | Apify scraper input |
| 2.2 Instagram URL | Phase 1: SCRAPE | Apify scraper input |
| 5.3 Websites you like | Phase 2: RESEARCH | Role model analysis |
| 5.4 Preferred style | Phase 2: RESEARCH | Design direction |
| 1.1-1.9 Business info | Phase 3: PLAN | Content for website |
| 3.1-3.6 Branding | Phase 4: DECIDE | BUILD-SPEC design system |
| 4.1-4.7 Services/content | Phase 4: DECIDE | BUILD-SPEC content |
| 5.1-5.7 Preferences | Phase 4: DECIDE | BUILD-SPEC structure |
| 6.1-6.6 Delivery | Phase 7: DELIVER | Deployment config |

---

## Tally.so Setup Tips

1. **Create form:** tally.so → New form → Multi-page
2. **Branding:** Upload your logo, set brand colors, choose a cover image
3. **Notifications:** Settings → Notifications → Add email
4. **Integration:** Settings → Integrations → Google Sheets (auto-record all responses)
5. **Sharing:** Get the link → Send to clients via LINE / email
6. **Pro tip:** Add a "thank you" page with your LINE QR code for instant follow-up
7. **Custom URL:** Use `tally.so/r/your-form-name` (free, cleaner than form ID)

## Google Sheets Integration

Set up Tally → Google Sheets auto-sync so every submission creates a row. Then you can:
- Track all leads in one spreadsheet
- Sort by status (new / in-progress / completed)
- Add columns for project stage, notes, billing

---

## Quick Tally.so Build Checklist

- [ ] Create form with 7 pages matching spec above
- [ ] Add conditional logic (5 branches)
- [ ] Enable file uploads on pages 3 & 4
- [ ] Set up Google Sheets integration
- [ ] Add email notification
- [ ] Set custom completion message (Thai)
- [ ] Brand with your logo & colors
- [ ] Test on mobile (most Thai clients will fill on phone)
- [ ] Create short link for sharing
