---
name: "Little Meow Pet Hospital"
repo: ""
tags: [veterinary, website, web-app]
status: active
created: 2026-03-05
---

# Little Meow Pet Hospital

> Conversion-optimized veterinary hospital website for a real clinic in Phitsanulok, Thailand — deployed on Cloudflare Pages.

## Problem

A local veterinary hospital specializing in complex orthopedic surgery, exotic animal care, acupuncture/rehabilitation, and boarding needed a professional web presence optimized for Thai pet owner conversion behavior (click-to-call, LINE inquiry, map guidance).

## Solution

A single-page static website built from scraped Facebook/Instagram content and role-model analysis (BondVet.com), following a hero-trust-value-close conversion flow adapted for Thai-local behavior. Fully static export for zero-cost hosting on Cloudflare Pages.

## Tech Stack

- **Framework**: Next.js 15 (App Router, static export)
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS v4 with custom design tokens
- **Fonts**: Sarabun (Thai + Latin) via next/font
- **Deployment**: Cloudflare Pages (static)
- **SEO**: JSON-LD VeterinaryCare schema, Open Graph, Thai-first meta

## Key Features

- 9-section conversion-optimized layout (nav, hero, trust strip, services, why us, gallery, about, contact, footer CTA)
- Click-to-call and Google Maps integration for Thai mobile-first users
- BondVet-inspired design adapted with teal/cream palette and Thai typography
- Masonry photo gallery from real hospital photos (61 images scraped from Facebook)
- Responsive design with mobile hamburger nav and full-width CTAs
- Structured data (JSON-LD) for local veterinary search visibility

## Highlights

- Live at [little-meow-pet-hospital.pages.dev](https://little-meow-pet-hospital.pages.dev)
- Built end-to-end from social media scraping to deployment in a single pipeline
- Static export — zero hosting cost on Cloudflare Pages free tier
- 4 specialty service cards: orthopedic surgery, exotic animals, acupuncture/rehab, boarding
