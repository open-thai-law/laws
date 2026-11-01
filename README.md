# กฎหมายไทยใน Git

[![validate](https://github.com/open-thai-law/laws/actions/workflows/validate.yml/badge.svg)](https://github.com/open-thai-law/laws/actions/workflows/validate.yml)
[![release](https://img.shields.io/github/v/release/open-thai-law/laws?label=release)](https://github.com/open-thai-law/laws/releases/latest)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23796239.svg)](https://doi.org/10.5281/zenodo.23796239)
[![license: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)

พระราชบัญญัติ พระราชกำหนด ประมวลกฎหมาย รัฐธรรมนูญ และประกาศคณะปฏิวัติ / คสช. **1,899 ฉบับ** เก็บเป็นไฟล์ Markdown หนึ่งไฟล์ต่อหนึ่งฉบับ ทุกครั้งที่กฎหมายถูกแก้คือหนึ่ง commit ลงวันที่ที่มีผลบังคับใช้ ผู้เขียน commit คือผู้ตรากฎหมายฉบับที่แก้

ใช้ git ดูได้ว่ามาตราไหนแก้เมื่อไร แก้โดยกฎหมายฉบับไหน และใครเป็นผู้ตรา

> [!WARNING]
> **ไม่ใช่ฉบับทางการ** ข้อความแปลงมาจากฐานข้อมูลของสำนักงานคณะกรรมการกฤษฎีกาโดยอัตโนมัติ อาจมีข้อผิดพลาด ห้ามใช้แทนฉบับที่ประกาศในราชกิจจานุเบกษา และไม่ใช่คำแนะนำทางกฎหมาย ตรวจกับต้นฉบับทุกครั้ง: [ราชกิจจานุเบกษา](https://ratchakitcha.soc.go.th) · [ระบบกลางทางกฎหมาย / กฤษฎีกา](https://searchlaw.ocs.go.th)

## ใช้งาน

```sh
git clone https://github.com/open-thai-law/laws.git
cd laws
git config core.quotepath false   # ให้ git แสดงชื่อไฟล์ภาษาไทย

# ประวัติทั้งหมดของ พ.ร.บ.คอมพิวเตอร์
git log --stat -- "acts/พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. ๒๕๕๐.md"

# แต่ละครั้งแก้อะไร (ทีละคำ)
git log -p --word-diff -- "acts/พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. ๒๕๕๐.md"

# แต่ละบรรทัดของประมวลรัษฎากรมาจากการแก้ครั้งไหน
git blame "acts/พ.ร.บ.ให้ใช้บทบัญญัติแห่งประมวลรัษฎากร พ.ศ. ๒๔๘๑.md"

# ใครตรากฎหมายมากที่สุด
git shortlog -sn
```

ตัวอย่างเพิ่มเติมใน [`examples/`](examples):

```sh
python3 examples/most_amended.py 10              # กฎหมายที่ถูกแก้บ่อยที่สุด
python3 examples/search.py "ข้อมูลส่วนบุคคล"       # มาตราที่พูดถึงคำนี้ ในกฎหมายที่ยังใช้บังคับ
examples/section-history.sh "acts/พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. ๒๕๕๐.md" ๑๔
                                                 # ทุกครั้งที่มาตรา ๑๔ ถูกแก้
```

หรือเปิดไฟล์บน GitHub แล้วกด **History** / **Blame** ได้เลย รายชื่อทุกฉบับอยู่ใน [`index.csv`](index.csv)

## โครงสร้าง

```
acts/<ชื่อกฎหมาย พ.ศ. ปี>.md   หนึ่งไฟล์ต่อหนึ่งฉบับ
index.csv                      ทุกฉบับ: ไฟล์ ชื่อ รหัสกฎหมาย สถานะ วันประกาศ จำนวนเวอร์ชัน ลิงก์
datapackage.json               คำอธิบายคอลัมน์ของ index.csv (Frictionless Data)
docs/schema.md                 รูปแบบไฟล์ frontmatter และ commit แบบละเอียด
examples/                      ตัวอย่างการใช้งาน (Python ไม่ต้องติดตั้งอะไรเพิ่ม, shell)
scripts/validate.py            ตรวจว่าข้อมูลถูกรูปแบบ รันทุก push
```

แต่ละไฟล์ (รายละเอียดครบใน [docs/schema.md](docs/schema.md)):

```markdown
---
title: "พระราชบัญญัติว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. ๒๕๕๐"
published: 2007-06-18          # วันประกาศในราชกิจจานุเบกษา
source: "searchlaw.ocs.go.th"
law_code: "…"                  # รหัสกฎหมายของกฤษฎีกา
status: in-force               # หรือ repealed
url: "https://searchlaw.ocs.go.th/…"
unofficial: true
---

# ชื่อกฎหมาย
คำปรารภ
## หมวด ๑ …
### มาตรา ๑
วรรคละหนึ่งบรรทัด
```

- หนึ่ง `### มาตรา` ต่อหนึ่งมาตรา หนึ่งบรรทัดต่อหนึ่งวรรค diff และ blame จึงตรงกับมาตราและวรรค
- ชื่อไฟล์ย่อ "พระราชบัญญัติ" เป็น "พ.ร.บ." และเก็บปีไว้ กฎหมายชื่อซ้ำ (รัฐธรรมนูญแต่ละฉบับ งบประมาณแต่ละปี) จึงแยกไฟล์กัน ชื่อที่ซ้ำกันหรือยาวเกินจะต่อรหัสกฎหมายไว้ท้ายชื่อ
- กฎหมายที่ยกเลิกแล้วยังอยู่ (`status: repealed`) พร้อมข้อความล่าสุดก่อนยกเลิก

## commit

| ส่วน | ความหมาย |
|---|---|
| ข้อความ | ชื่อกฎหมายฉบับที่แก้ + วันที่มีผลบังคับใช้ + เชิงอรรถของกฤษฎีกาว่ามาตราไหนแก้โดยฉบับไหน |
| วันที่ | วันที่มีผลบังคับใช้ |
| ผู้เขียน (author) | ผู้ตรากฎหมายฉบับที่แก้ ตามลำดับ: สภาที่ระบุในคำปรารภ → ผู้ออกที่ระบุในชื่อ (คณะปฏิวัติ, คสช. ฯลฯ) → พระมหากษัตริย์ สำหรับกฎหมายก่อน 24 มิ.ย. 2475 → คณะรัฐมนตรี สำหรับพระราชกฤษฎีกา / พระราชกำหนด → สภาที่ตรากฎหมายในช่วงเวลานั้น (อนุมานจากกฎหมายฉบับใกล้เคียง และเขียนบอกไว้ใน commit) |

ข้อจำกัดที่รู้อยู่:

- **git เก็บวันที่ก่อนปี 1970 ไม่ได้** commit ที่เก่ากว่าลงวันที่ 1970-01-02 วันจริงอยู่ในบรรทัด `มีผลบังคับใช้` ของข้อความ commit
- ราว 190 ฉบับ (ส่วนใหญ่ยกเลิกแล้ว) ต้นทางมีแค่ข้อความ "โปรดดูรายละเอียดที่ราชกิจจานุเบกษา" ยังไม่มีตัวบท
- ผู้ตรายังระบุไม่ได้ 47 commit (ส่วนใหญ่เป็นรัฐธรรมนูญฉบับชั่วคราว) ใช้ชื่อ "ไม่ระบุ" ดีกว่าเดาผิด
- ชื่อผู้ตราบางอันสะกดตามต้นฉบับซึ่งต่างกันเล็กน้อย เช่น "ปฏิรูป" / "ปฎิรูป"
- ยังไม่มีกฎหมายลำดับรอง (พระราชกฤษฎีกาออกตามความใน… กฎกระทรวง ประกาศกระทรวง)

## ที่มาของข้อมูลและสิทธิ์

- ตัวบทและประวัติการแก้ไขมาจาก [ระบบค้นหากฎหมายของสำนักงานคณะกรรมการกฤษฎีกา](https://searchlaw.ocs.go.th) (ฉบับรวมและเชิงอรรถ) และรายชื่อกฎหมายจาก [www.ocs.go.th](https://www.ocs.go.th/searchlaw-law)
- ตัวบทกฎหมายไม่มีลิขสิทธิ์ตาม [พ.ร.บ.ลิขสิทธิ์ พ.ศ. ๒๕๓๗ มาตรา ๗](acts/พ.ร.บ.ลิขสิทธิ์%20พ.ศ.%20๒๕๓๗.md)
- ส่วนที่เราจัดทำ (โครงสร้างไฟล์ ประวัติ commit ผู้ตรา `index.csv`) อุทิศเป็นสาธารณสมบัติด้วย [CC0 1.0](LICENSE) ใช้ได้ทุกวัตถุประสงค์ ไม่ต้องขออนุญาต ถ้าอ้างอิงกลับมาจะขอบคุณมาก

## อ้างอิง

กดปุ่ม **Cite this repository** ด้านขวาของหน้า repo หรือใช้ [`CITATION.cff`](CITATION.cff) ระบุ release ที่ใช้ด้วย (ชื่อ tag คือวันที่ดึงข้อมูล เช่น `2026-10-30`) เพื่อให้คนอื่นได้ข้อมูลชุดเดียวกัน ทุก release เก็บถาวรที่ Zenodo: DOI [10.5281/zenodo.23796239](https://doi.org/10.5281/zenodo.23796239) ชี้ไปฉบับล่าสุดเสมอ ส่วนแต่ละ release มี DOI ของตัวเองในหน้า Zenodo

## ช่วยกัน

เจอข้อความผิด มาตราหาย หรือกฎหมายที่แก้แล้วแต่ที่นี่ยังไม่อัปเดต แจ้งได้ที่ [Issues](../../issues/new/choose) อ่านวิธีใน [CONTRIBUTING.md](CONTRIBUTING.md) และ [จรรยาบรรณ](CODE_OF_CONDUCT.md) ช่องโหว่หรือเนื้อหาอันตรายแจ้งแบบส่วนตัวตาม [SECURITY.md](SECURITY.md)

---

## English

Thai primary legislation (1,899 acts, codes, constitutions, emergency decrees and junta orders) as a git repository: one Markdown file per law, one commit per amendment, dated by when it took effect and authored by the body that enacted the amending law. Use `git log -p`, `git blame` and `git shortlog` to see what changed, when, by which act and by whom.

**Unofficial.** Converted automatically from the Office of the Council of State's database; may contain errors and is not legal advice. Check the Royal Gazette. Law text is not copyrightable in Thailand (Copyright Act B.E. 2537, Section 7); our structure, history and index are released under CC0 1.0. Report errors in [Issues](../../issues/new/choose).

ริเริ่มโดย [breakfastz](https://breakfastz.dev)
