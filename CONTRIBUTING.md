# ช่วยกันทำให้ข้อมูลถูกต้อง

ขอบคุณที่ช่วยครับ ทุกไฟล์ใน `acts/` **สร้างอัตโนมัติ** จากฐานข้อมูลของสำนักงานคณะกรรมการกฤษฎีกา ถ้าแก้ไฟล์ตรงๆ รอบอัปเดตถัดไปจะเขียนทับ เราจึงรับการแก้ข้อมูลผ่าน **Issue** แล้วผู้ดูแลจะแก้ที่ตัวแปลงหรือบันทึกเป็นการแก้ไขถาวร คนที่แจ้งจะถูกให้เครดิตใน commit

## แจ้งอะไรได้บ้าง

| เจออะไร | แจ้งด้วยแบบฟอร์ม |
|---|---|
| ข้อความไม่ตรงกับราชกิจจานุเบกษา: ตัวสะกด สระหาย มาตราหรือวรรคหาย ลำดับผิด | [ข้อความผิด](../../issues/new?template=text-error.yml) |
| กฎหมายแก้ไขแล้ว (ลงราชกิจจาฯ แล้ว) แต่ที่นี่ยังเป็นฉบับเก่า | [ยังไม่อัปเดต](../../issues/new?template=outdated.yml) |
| กฎหมายที่ยังไม่มีใน repo | [ขอเพิ่มกฎหมาย](../../issues/new?template=missing-law.yml) |
| ผู้ตรา (author) หรือวันที่ของ commit ผิด | [ประวัติผิด](../../issues/new?template=history-error.yml) |

แนบหลักฐานจากต้นฉบับเสมอ: ลิงก์ราชกิจจานุเบกษา (เล่ม / ตอน / หน้า) หรือหน้าของกฤษฎีกา เราตรวจกับต้นฉบับก่อนแก้ทุกครั้ง

## Pull request

- **รับ:** แก้ README / CONTRIBUTING, ตัวอย่างการใช้งาน, เครื่องมือหรือสคริปต์ที่อ่านข้อมูลนี้ (ใส่ไว้ใน `examples/`)
- **ก่อนส่ง:** รัน `python3 scripts/validate.py` ให้ผ่าน (ระบบจะรันให้อีกรอบทุก PR) รูปแบบข้อมูลอยู่ใน [docs/schema.md](docs/schema.md)
- **ไม่รับ:** แก้ไฟล์ใน `acts/` หรือ `index.csv` ตรงๆ (จะถูกเขียนทับ) ให้เปิด issue แทน

## ไม่ใช่ที่ปรึกษากฎหมาย

repo นี้เก็บตัวบทอย่างเดียว คำถามว่ากฎหมายใช้กับกรณีของเรายังไง ควรถามทนายความหรือหน่วยงานที่เกี่ยวข้อง issue ที่เป็นคำถามทางกฎหมายจะถูกปิด

## มารยาท

ทุกคนในโปรเจกต์นี้ยึด[จรรยาบรรณ (Contributor Covenant)](CODE_OF_CONDUCT.md) คุยกันด้วยข้อเท็จจริงและความสุภาพ ไม่ถกเถียงการเมืองใน issue ผู้ตราใน commit มาจากเอกสารต้นฉบับ ไม่ได้แสดงความเห็นของผู้ดูแล

---

**English:** Files in `acts/` are generated from the Council of State's database, so please report errors, outdated laws or missing laws as [issues](../../issues/new/choose) with a link to the Royal Gazette rather than editing them. Pull requests are welcome for docs and examples; run `python3 scripts/validate.py` first. See the [schema](docs/schema.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).
