# SWU DS525 - Capstone Project
![alt text](Archive/header.jpg) 

จากการสำรวจสถิติการเกิดอุบัติเหตุบนถนนขององค์การอนามัยโลกในปี 2561 ประเทศไทยถูกจัดให้เป็นประเทศที่มีอัตราการเกิดอุบัติเหตุบนถนนสูงสุดเป็นอันดับที่ 9 ของโลก โดยไทยมีความพยายามในการลดอุบัติเหตุด้วยวิธีต่างๆอย่างต่อเนื่อง โดยเน้นที่การแก้ไขโครงสร้างพื้นฐาน ระบบโลจิสติกส์ และดิจิทัล เพื่อให้สามารถลดอัตราการเกิดอุบัติเหตุบนถนนภายในระยะเวลา 3 ปีข้างหน้าหรือปี พ.ศ. 2570
ดังนั้น บทบาทของเรา คือ วิเคราะห์ข้อมูลเพื่อหาแนวทางในการแก้ไขปัญหาและมุ่งหวังเป็นส่วนหนึ่งในการช่วยลดอุบัติเหตุบนท้องถนนในประเทศไทย
# Documentation
## 1. Dataset
Data.go.th หรือ ศูนย์กลางข้อมูลภาครัฐ โดยกลุ่มของพวกเราเลือกใช้ข้อมูลผู้เสียชีวิตจากอุบัติเหตุทางถนน จากระบบบูรณาการข้อมูลการเสียชีวิตจากอุบัติเหตุทางถนน (3 ฐาน)
- ข้อมูลผู้เสียชีวิตจากอุบัติเหตุทางถนน (โดยกลุ่มพวกเราใช้ข้อมูลในปี 2563 - 2565) : [link](https://data.go.th/dataset/rtddi)


## 2. Problem & Target
**Problem**
1. ตรวจสอบการกระจายตัวของพื้นที่ที่เกิดอุบัติเหตุทางท้องถนน ตลอดช่วงเวลาที่ผ่านมา มีจุดเกิดเหตุเกิดขึ้นบริเวณใดบ้าง โดยแบ่งเป็นกลุ่มพื้นที่ตามจังหวัดต่างๆ
2. ทำความเข้าใจลักษณะที่เกิดขึ้นบ่อยๆ โดยการตรวจสอบหาปัจจัยที่คาดว่าจะมีผลกับการเกิดอุบัติเหตุ เช่น การเสียชีวิตจากอุบัติเหตุทางถนน เกิดจากพาหนะประเภทใดเป็นหลัก เกิดขึ้นกับเพศไหน คนขับ หรือผู้เสียชีวิตอายุเท่าไหร่ ฤดูกาลมีผลต่อการเกิดอุบัติเหตุหรือไม่




**Target**
* เพื่อทำความเข้าใจลักษณะของอุบัติเหตุที่มักเกิดขึ้นบ่อยครั้งในแต่ละจังหวัดในประเทศไทย โดยพิจารณาเรื่อง เพศ อายุ ประเภทของพาหนะที่เกี่ยวข้อง รวมถึงฤดูกาลที่เกิดเหตุ มาเป็นปัจจัยในการวิเคราะห์ โดยใช้ข้อมูลจากจำนวนการเกิดอุบัติเหตุในปี 2563 - 2565, ประเทศไทย นำมาหาว่าจังหวัดใดมีอัตราการเสียชีวิตสูงสุด 
 สามารถนำข้อมูลที่ได้มาวิเคราะห์ หาinsight เพื่อนำข้อมูล และข้อสรุปมาเสนอแนะแนวทางการแก้ไข ให้หน่วยงานและผู้ที่มีส่วนเกี่ยวข้องในความรับผิดชอบช่วยกันหาแนวทางเพื่อลดการเกิดอุบัติเหตุบนท้องถนนในประเทศไทย โดยอาจจะเป็นการปรับปรุงโครงสร้างพื้นฐาน ระบบโลจิสติกส์ และการใช้เทคโนโลยีดิจิทัล เพื่อรณรงค์การลดอุบัติเหตุที่เกิดขึ้นบนท้องถนน



## 3. Data model
![alt text](Archive/image/data_model.jpg)



Data model มีองค์ประกอบ ดังนี้
**1) Entity (เอนทิตี)**
* case_info (ข้อมูลการเกิดเหตุ): เก็บข้อมูลเกี่ยวกับเคสอุบัติเหตุ
* personal_info (ข้อมูลส่วนบุคคล): เก็บข้อมูลเกี่ยวกับผู้เสียชีวิต
* vehicle_info (ข้อมูลยานพาหนะ): เก็บข้อมูลทั้งหมดเกี่ยวกับบัญชีจำแนกทางสถิติระหว่างประเทศของโรคและปัญหาสุขภาพที่เกี่ยวข้อง เป็นรหัสของโรคและอาการ อาการแสดง ความผิดปกติที่ตรวจพบ อาการนำ สภาพสังคม หรือสาเหตุภายนอกของการบาดเจ็บหรือโรค




**2) Attribute (แอตทริบิวต์)**
* acc_dead_id (รหัสคดีผู้เสียชีวิต): รหัสประจำตัวเคสผู้เสียชีวิต
* personal_id (รหัสประจำตัวบุคคล): รหัสประจำตัวผู้เสียชีวิต
* psn_dead_year (ปีเสียชีวิต): ปีที่ผู้เสียชีวิตเสียชีวิต
* psn_sex (เพศเสียชีวิต): เพศของผู้เสียชีวิต
* psn_age (อายุเสียชีวิต): อายุของผู้เสียชีวิต
* psn_tumbol (ตำบลเสียชีวิต): ตำบลของผู้เสียชีวิต
* psn_district (อำเภอเสียชีวิต): อำเภอที่เสียชีวิต
* psn_province (จังหวัดเสียชีวิต): จังหวัดที่เสียชีวิต
* psn_nataionality (เชื้อช่าติเสียชีวิต): เชื้อชาติของผู้เสียชีวิต
* actual_dead_date (วันที่เสียชีวิตจริง): วันที่ผู้เสียชีวิตเสียชีวิต
* case_time (เวลาเกิดเหตุ): เวลาที่เกิดเหตุ
* case_tumbol (ตำบลเกิดเหตุ): ตำบลที่เกิดเหตุ
* case_district (อำเภอเกิดเหตุ): อำเภอที่เกิดเหตุ
* case_province (จังหวัดเกิดเหตุ): จังหวัดที่เกิดเหตุ
* case_lat (ละติจูด): ละติจูดของจุดเกิดเหตุ
* case_long (ลองจิจูด): ลองจิจูดของจุดเกิดเหตุ
* icd_code (รหัส ICD): รหัสสาเหตุการเสียชีวิตตามมาตรฐาน ICD
* vehicle_name (ประเภทของยานพาหนะ): ประเภทของยานพาหนะที่เกี่ยวข้องกับเหตุ






**3) Relationship (ความสัมพันธ์)**
* case_info (ข้อมูลการเกิดอุบัติเหตุ) มีความสัมพันธ์ 1:1 กับ personal_info (ข้อมูลส่วนบุคคล): หมายความว่า การเกิดอุบัติเหตุในแต่ละเคสจะมีผู้เสียชีวิตหนึ่งคน
* case_info (ข้อมูลการเกิดอุบัติเหตุ) มีความสัมพันธ์ 1:1 กับ vehicle_info (ประเภทของยานพาหนะ): หมายความว่า การเกิดอุบัติเหตุในแต่ละเคสจะมียานพาหนะที่เกี่ยวข้องเพียงหนึ่งยานพาหนะ

### Data Model for Dashboard

![alt text](Archive/image/aa.jpg)

* accident_case_obt (ข้อมูลการเกิดเหตุเต็มรูปแบบ): เก็บข้อมูลทั้งหมดเกี่ยวกับเคสอุบัติเหตุและข้อมูลผู้เสียชีวิต
หมายเหตุ : สำหรับ accident_case_obt คือ One Big Table (OBT) สำหรับ Dashboard

## 4. Data Pipeline
![alt text](Archive/data_pipeline.png)
**1) การเก็บรวบรวมข้อมูล (Data Ingestion):** Raw Data จากเว็บไซต์ data.go.th ด้วย API ดึงเข้าสู่ระบบคลาวด์สตอเรจ ในที่นี้คือ Google Cloud Storage เพื่อเก็บไฟล์ไว้ในรูปแบบ CSV file โดยกำหนดให้ไฟล์ที่ถูกดึงมาจาก API ประกอบด้วยชื่อไฟล์ และวันที่ทำการดึงข้อมูล ซึ่งทางกลุ่มได้ทำการ Automate ขั้นตอนนี้ด้วย Airflow
* สาเหตุที่ทางกลุ่มเลือกใช้ API เนื่องจากเป็นการช่วยให้ Workflow สามารถ Automate ได้ง่ายขึ้นไม่ต้องทำการ Download ข้อมูลที่จะสร้างความซับซ้อนให้แก่กระบวนการทำงานแบบอัตโนมัติ


**2) การโหลดข้อมูล (Data Loading):** ขั้นตอนต่อมาข้อมูลจะถูกโหลดเข้าสู่คลังข้อมูล (Data Warehouse) ในที่นี้กลุ่มเราใช้ Google BigQuery โดยในขั้นตอนนี้เรามีการ Transform ข้อมูลด้วยการสร้าง Table ปรับปรุง Table และทำการ Partitioning Table


**3) การเปลี่ยนแปลงหรือแก้ไขข้อมูล (Data Transformation):** ในขั้นตอนนี้ในการ Transform ข้อมูลอีกครั้งด้วยการสร้าง Staging layer และ Reporting layer ด้วยการสร้าง View จาก Table ที่สร้างในขั้นตอนข้างต้น
* ในการเลือกใช้ dbt ทางกลุ่มมองว่าการสร้าง Model ต่างๆผ่าน dbt สามารถส่งต่อหรือแชร์ script ของ Model เพื่อให้ผู้ที่เกี่ยวข้องสามารถอ่านข้อมูลจาก SQL ได้เช่นเดียวกัน และยังสามารถ Reproduct script ได้อีกเช่นกัน


**4) การวิเคราะห์ข้อมูล (Data Analysis):** เมื่อข้อมูลถูก Transform ให้พร้อมเรียบร้อยแล้ว ขั้นตอนต่อไปจะนำไปวิเคราะห์โดยใช้เครื่องมือต่าง ๆ โดยกลุ่มของพวกเราใช้ Looker Studio เพื่อสร้างรายงานและข้อมูลเชิงลึก ผ่าน Visualization





## 5. Visualization
![alt text](Archive/image/pic24.jpg)

**Analytics result (ผลการวิเคราะห์)**
- จังหวัดที่มีอัตราการเกิดอุบัติเหตุสูงสุดต่อวัน 3 อันดับแรกได้แก่
1. จังหวัดกรุงเทพมหานคร 658 ครั้ง
2. จังหวัดนครราชสีมา 654 ครั้ง
3. จังหวัดชลบุรี 547 ครั้ง
- ช่วงอายุที่มีผู้เสียชีวิตสูงสุด 3 อันดับแรก ได้แก่
1. 36-60 ปี ร้อยละ 37.6%
2. 60 ปีขึ้นไป ร้อยละ 24.9%
3. 25-35 ปี ร้อยละ 17.7%
- การเสียชีวิตจากอุบัติเหตุทางถนน โดยพิจารณาจากปัจจัยเรื่องเพศ พบว่าเพศชายมีอัตราการเสียชีวิตมากกว่าเพศหญิงอย่างมีนัยสำคัญ ดังนี้
1. ปี 2023 เพศชาย จำนวน 7,691 ราย, เพศหญิง จำนวน 2,309 ราย 
2. ปี 2022 เพศชาย จำนวน 1,982 ราย, เพศหญิง จำนวน 518 ราย 
3. ปี 2021 เพศชาย จำนวน 1,635 ราย, เพศหญิง จำนวน 395 ราย 
ซึ่งมีแนวโน้มไปในลักษณะทิศทางเดียวกันตลอดสามปี(2021-2023)โดยปี 2023 ค่อนข้างมีอัตราการเสียชีวิตที่พุ่งสูงขึ้นจากสองปีก่อนหน้า
- ฤดูกาลที่มีผู้เสียชีวิตสูงสุดตามลำดับ ได้แก่
1. ฤดูฝน ร้อยละ 35.1%
2. ฤดูร้อน ร้อยละ 32.9%
3. ฤดูหนาว ร้อยละ 32.1%
- การเสียชีวิตจากอุบัติเหตุทางถนน เกิดจากพาหนะประเภทรถจักรยานยนต์สูงสุด รองลงมาเป็นรถยนต์ และสุดท้ายคือ รถบรรทุกขนาดเล็ก/รถตู้ โดยแนวโน้มของทั้งสามปี(2021-2023)มีลักษณะไปในทิศทางเดียวกันและปีที่มีการเสียชีวิตสูงสุดคือปี 2023, 2022 และ 2021 ตามลำดับ
1. ปี 2023 รถจักรยานยนต์ จำนวน 5,415 ราย, รถยนต์ จำนวน 702 ราย, รถบรรทุกขนาดเล็ก จำนวน 248 ราย
2. ปี 2022 รถจักรยานยนต์ จำนวน 1,183 ราย, รถยนต์ จำนวน 138 ราย, รถบรรทุกขนาดเล็ก จำนวน 70 ราย
3. ปี 2021 รถจักรยานยนต์ จำนวน 1,122 ราย, รถยนต์ จำนวน 109 ราย, รถบรรทุกขนาดเล็ก จำนวน 47 ราย



**Discussion (อภิปรายผลการวิเคราะห์ข้อมูล)**
นอกจากมาตรการโดยทั่วไปที่ภาครัฐได้มีการแก้ไขและพัฒนาอย่างต่อเนื่อง เช่น การแก้ไขโครงสร้างขั้นพื้นฐาน อย่่างการเพิ่มความสว่าง,แก้ไขจุดดำบนถนน หรือด้านดิจิทัลอย่างการใช้เทคโนโลยีในการตรวจจับความเร็ว 
จาก Visualization ที่ได้ทำให้เราเห็น Insight ของข้อมูลผู้เสียชีวิตจากอุบัติเหตุทางถนน และอาจบ่งชี้ถึงปัญหาและแนวทางในการลดจำนวนการเสียชีวิตจากอุบัติเหตุได้อย่างมีประสิทธิภาพมากยิ่งขึ้น 
1) พื้นที่ที่มีจำนวนผู้เสียชีวิตสูงสุดไล่เลี่ยกัน 3 อันดับ คือ จังหวัดกรุงเทพมหานคร จังหวัดนครราชสีมา และชลบุรี ซึ่งสอดคล้องกับจำนวนประชากรและยานพาหนะในพื้นที่ ทำให้มีผู้ใช้ถนนจำนวนมาก 
ซึ่งแนวทางในการแก้ไขปัญหาที่เกิดขึ้น เช่น การพัฒนาระบบขนส่งสาธารณะเพื่อกระตุ้นให้ประชาชนใช้ขนส่งสาธารณะมากขึ้น ซึ่งอาจเป็นส่วนช่วยให้มีการลดจำนวนผู้ใช้ถนนได้
2) ช่วงอายุที่มีผู้เสียชีวิตสูงสุดสามอันดับแรก คือ วัยทำงาน (36-60 ปี), ผู้สูงอายุ (60 ปีขึ้นไป) และวัยรุ่น (25-35 ปี) ตามลำดับ โดยข้อมูลมีความสอดคล้องกับพฤติกรรมการขับขี่และความเสี่ยงทางสุขภาพของแต่ละช่วงอายุ ดังนั้น กลุ่มเป้าหมายที่ต้องให้ความสำคัญเป็นพิเศษ คือ วัยผู้ใหญ่โดยวัยทำงานเป็นช่วงที่วัยที่ขับขี่ด้วยความรีบเร่งและเหนื่อยล้าจากการทำงานหรือจากการสังสรรค์ ซึ่งอาจจะใช้เทคโนโนโลยีเข้ามาช่วยลดอุบัติเหตุ เช่น ระบบเตือนเมื่อออกนอกเลน ระบบตรวจจับการใช้โทรศัพท์มือถือขณะขับขี่ หรือการรณรงค์ให้พักผ่อนให้เพียงพอและเข้มงวดกับมาตรการดื่มไม่ขับมากยิ่งขึ้น
3) เพศชายมีอัตราการเสียชีวิตมากกว่าผู้หญิงอย่างมีนัยสำคัญ จึงควรให้ความสำคัญเป็นอย่างมาก ซึ่งอาจเนื่องมาจากพฤติกรรมและปัจจัยทางสังคม เช่น เพศชายมีแนวโน้มขับขี่ด้วยความเร็วสูงและชอบเสี่ยง ซึ่งถูกกระตุ้นจากฮอร์โมนของเพศชาย จึงส่งผลต่อพฤติกรรม หรือปัจจัยทางสังคม เช่น อาชีพที่มีความเสี่ยงภัยบนถนน อย่างการขับขี่ขนส่งเป็นต้น ดังนั้นมาตรการที่สามารถจะช่วยลดการเกิดอุบัติเหตุในเพศชายได้ เช่น การรณรงค์เน้นกลุ่มเพศชายเพื่อปรับเปลี่ยนทัศนคติเกี่ยวกับความเสี่ยง 
4) ช่วงเวลาในการเกิดอุบัติเหตุสูงสุด คือ ฤดูฝน, ฤดูร้อน และฤดูหนาวตามลำดับ ถึงแม้ว่าสัดส่วนจากการเกิดอุบัติเหตุในแต่ละชาวงเวลาจะไม่แตกต่างกันมากนะ แต่สามารถเพิ่มมาตรการเพื่อสนับสนุนให้จำนวนผู้เสียชีวิตลดลงได้ ดังนั้นอาจแก้ไขด้วยการเข้มงวดการบังคับใช้กฎจราจร โดยเฉพาะในช่วงฤดูฝนและช่วงเทศกาล
5) ประเภทพาหนะที่มีการเกิดอุบัติเหตุสูงสุด คือ รถจักรยานยนต์ ซึ่งสาเหตุจากมาจากปัจจัยด้านความเสี่ยงโดยธรรมชาติของรถจักรยานยนต์ เนื่องจากตัวรถมีขนาดเล็ก น้ำหนักเบา ทำให้ควบคุมทรงยาก หรือระบบการป้องกันภัยที่ไร้ระบบป้องกันผู้ขับขี่ เช่น ถุงลมนิรภัย เข็มขัดนิรภัย รวมไปถึงความมั่นคงขแงศูนย์ถ่วงสูง เสี่ยงต่อการล้มคว่ำได้ อาจแก้ไขปัญหาด้วยการควบคุมการดัดแปลงสภาพรถ หรือเข้มงวดกับการตรวจสภาพรถการใช้งาน รวมไปถึงปลูกฝังจิตสำนึกของผู้ขับขี่


ทั้งนีั้ ยังมีปัจจัยอื่นๆที่มีผลกับจำนวนผู้เสียชีวิตเนื่องจากอุบัติเหตุบนถนนได้อีก อย่างเช่น จำนวนผู้เสียชีวิตในปี 2023 ที่มีจำนวนมากกว่าปีอื่นๆมาก ซึ่งอาจสันนิษฐานได้ว่า เป็นช่วงการกกลับมาใช้ชีวิตหลังสภาวะโรระบาด covid19 ทำให้ผู้คนเดินทางมากขึ้น หรืออาจเกิดจากสภาวะเศรษฐกิจกต่ำ ทำให้คนมาใช้ยาานพาหนะที่ราคาไม่สูงเมื่อเทียบกับพาหนะอื่นๆ อย่างเช่น รถจักรยานยนต์ เป็นต้น
ซึ่งจาก Insight ที่ได้สามารถนำไปสู่การแก้ไขปัญหา โดยปัจจจัยที่ควรให้ความสำคัญในการเร่งแก้ไขเป็นอันดับต้นๆ คือ ประเภทของยานพาหนะ,ปัจจัยทางเพศ,ปัจจัยเรื่องช่วงอายุกับพฤติกรรมการขับขี่,ปัจจัยทางด้านพื้นที่ และในส่วนสุดท้าย คือ ปัจจัยทางด้านฤดูกาล



# Instruction
## 1. สร้าง ENV and Set Up
* สร้าง Folder  07-Capstone project
เข้าสู่หน้า  07-Capstone project  ด้วย 
```sh
$ cd 07-Capstone-project/
```
* สร้าง Environment ในการทำ python
```sh
$ python -m venv ENV
```
* Active ENV เพื่อเก็บสิ่งที่ให้งานไว้ใน ENV -> bin
```sh
$ source ENV/bin/activate
```
![alt text](Archive/pic1.png)


## 2. Cloud Storage
2.1 สร้าง  New project


![alt text](Archive/image/pic2.png)
* ไปที่หน้าเว็บ Google cloud platform (GCP) สร้าง New project   → “mycapstone”


2.2 สร้าง buckert:


* ไปที่  Google cloud platform (GCP) → cloud storage เพื่อสร้าง bucket  “swu-ds525-8888” เพื่อดึงข้อมูลจาก source open data มาเก็บไว้ใน bucket


* กด create

![alt text](Archive/image/pic3.jpg)

* ใส่ชื่อ bucket ชื่อ ” ds525_data_capstone”

![alt text](Archive/image/pic4.jpg)

![alt text](Archive/image/pic5.jpg)

2.3 สร้าง key ในการใช้งานเพื่อเชื่อมต่อ  Google cloud platform (GCP)  กับ Airflow
กด IAM & Admin → เลือก  service account  → create service account

![alt text](Archive/image/pic7.png)

* หน้าเมื่อสร้าง service account เสร็จ

![alt text](Archive/image/pic8.png)


* เมื่อสร้าง service account เสร็จให้ทำการเลือก service account ที่สร้าง → กดเลือก KEYS → ADD KEY → เลือก .json file → จะได้ keys file ที่เป็น json มาเก็บไว้ที่เครื่อง

![alt text](Archive/image/pic9.png)

* ทำการสร้าง folder credentials ใน github codespace เพื่อ upload file keys json ไปไว้ แต่ให้นำชื่อ folder credentials ไปใส่ใน file .gitignore เพื่อป้องกัน keys ของเราถูกในภายนอกนำไปใช้ 


## 3. Data Warehouse


3.1 เปิดการใช้งาน docker บน github codespace   
```sh
$ docker compose up
```
3.2  บน github codespace ไปที่ port 8080 เพื่อเปิดการใช้งาน Airflow บน browser


* กด open in Browser 8080


![alt text](Archive/image/pic10.png)

* เมื่อเปิด browser  จะแสดงหน้าให้ login เข้าสู่ระบบ


![alt text](Archive/image/pic11.png)

* เมื่อ login เรียบร้อยจะเข้าสู่หน้าการใช้งาน Airflow


![alt text](Archive/image/pic12.png)

* หน้า Airflow → เลือก Admin → Connections → สร้าง Connection → project id ใช้จาก GCP


![alt text](Archive/image/pic13.png)

3.3 Data pipeline โดยใช้ airflow ในการ Automated


* นำข้อมูลที่ได้จากการสร้าง project และ  bucket ใน GCP (ข้อ 2) และ Connection ใน airflow (ข้อ 3) มาใส่ใน file  acc_api_etl_pipeline.py


3.3.1 ตัวอย่าง Configuration ใน file  acc_api_etl_pipeline.py


* Get file

![alt text](Archive/pic13.png)

* Creating DAG to automate workflow with Airflow 

![alt text](Archive/pic14.png)

* Upload file to google cloud storage (GCS)


![alt text](Archive/pic15.png)

* Create bigquery  dataset


![alt text](Archive/pic16.png)

* Load data to bigquery


![alt text](Archive/pic17.png)

* Create table prep


![alt text](Archive/pic18.png)

* Create table case_info


![alt text](Archive/pic19.png)

* Create table personal_info


![alt text](Archive/pic20.png)

* Create table vehicle_info


![alt text](Archive/image/pic14.png)

* Setting workflow


```sh
start >> get_files_api >> upload_to_gcs >> [create_bq_raw_dataset, create_bq_dataset] >> follow_create_dataset >> [load_to_bq, load_raw_to_bq] >> table_prep >> [create_case_table, create_person_table, create_vehicle_table] >> end
```



* เมื่อทำการ run บน airflow ผ่าน flow task จะแสดงเป็นสีเขียวทั้งหมด


![alt text](Archive/pic47.png)

3.4 เมื่อรัน Airflow แบบ Automated เสร็จ

3.4.1 บนหน้า google cloud storage → bucket จะมี file ข้อมูลที่ถูกดึง มาวางไว้ใน bucket
3.4.2 บนหน้า google cloud platform → bigquery

* แบ่ง dataset 2 คือ  project_accident เพื่อเก็บข้อมูลที่ต้องการ transform และ project_accident_raw เพื่อเก็บข้อมูล raw data เนื่องจากเพื่อป้องกันการเปลี่ยนแปลงข้อมูลในตัวข้อมูล raw 


![alt text](Archive/image/pic15.png)

* Dataset : project_accident จะมี 3 table คือ accident_case_full , case_info , personal_info , vehicle_info


![alt text](Archive/pic48.png)


* Table : accident_case_full


![alt text](Archive/pic49.png)

* Table : Case_info  (partitioned table) ทำ partition ด้วย column actual_dead_date


![alt text](Archive/pic50.png)


* Table : Personal_info (partitioned table) ทำ partition ด้วย column psn_dead_year


![alt text](Archive/pic51.png)

* Table : vehicle_info 


![alt text](Archive/pic52.png)


## 4. Data Transformation (DBT)

4.1 ใช้ github codespace ทำการ install dbt
```sh
$ pip install dbt-core dbt-bigquery
```

![alt text](Archive/image/pic16.png)

4.2 สร้าง project ในการทำ dbt
```sh
$ dbt init
```
* เมื่อสร้าง project เสร็จจะมี folder capstoneproject สร้างขึ้นมา

![alt text](Archive/image/pic17.png)

4.3 สร้าง file profile.yml เก็บใน folder capstoneproject
```sh
code /home/codespace/.dbt/profiles.yml
```


* เมื่อรัน code เสร็จจะมี file profile.yml - dbt ขึ้นมาให้ copy ข้อมูลข้างใน file ไปใส่ใน folder project_accident – > create file profile.yml แล้วข้อมูลนำไปใส่


![alt text](Archive/image/pic18.png)

4.4 ทำการ Check connection ว่า dbt ถูกเชื่อมต่อกับ google bigquery  → เมื่อทำการเชื่อมต่อสำเร็จจะขึ้น All checked passed!


```sh
$ dbt debug
```
![alt text](Archive/image/pic19.png)

4.5 ทำการ create layer เพื่อ transform ข้อมูล


4.5.1 สร้าง table ที่จะทำการ staging  และ view


จาก Path  : 07-capstone-project/capstoneproject/model ทำการสร้าง 2  folder ใน folder model คือ Folder view , Folder staging


* Folder : staging ทำการแบ่ง staging ออกเป็น 3 ตาราง
1) File : stg__case_info.sql

![alt text](Archive/image/pic35.png)

2) File : stg__personal_info.sql

![alt text](Archive/image/pic36.png)

2) File : stg__vehicle_info.sql

![alt text](Archive/image/pic37.png)

* Folder : view  ทำการสร้าง view เพื่อตอบปัญหา โดยแบ่งออกเป็น view 6 ตารางดังนี้

1) File : view_accident_obt.sql

หลังจากที่ได้ทำการ Transform และสร้างตารางผ่าน Bigquery ในขั้นตอนก่อนหน้าแล้ว เราจะทำการสร้าง view_accident_obt (One Big Table) เพื่อเป็น Data Model ใน Reporting layer โดยอ้างอิงจากตาราง accident_case_full


![alt text](Archive/image/pic20.png)

2) File : acc_by_age.sql


![alt text](Archive/image/pic28.png)


3) File : acc_by_province.sql


![alt text](Archive/image/pic29.png)


4) File : acc_by_seasons.sql


![alt text](Archive/image/pic30.png)


5) acc_by_sex.sql


![alt text](Archive/image/pic31.png)


6) acc_by_vehicle.sql


![alt text](Archive/image/pic33.png)



4.5.2 ทำการ  run automate test → เพื่อ check code ก่อนที่จะ run จริง
```sh
$ dbt test
```


![alt text](Archive/image/pic21.png)


4.5.3 ทำการ run dbt 
```sh
$ dbt run
```


![alt text](Archive/image/pic22.png)

4.5.4 เมื่อทำการรัน dbt run ผ่าน → กลับไปหน้า google bigquery → จะมี table staging กับ view แสดงขึ้นมา

![alt text](Archive/image/pic34.png)





## 5. Data Visualization


5.1 ใช้ Looker Studio ในการทำ Data Visualization


* เปิด หน้า  Looker Studio → blank report เพื่อสร้าง dashboard


![alt text](Archive/image/pic25.png)




* เลือก bigquery


![alt text](Archive/image/pic26.png)


* เลือก project “mycapstone” →  dataset “project_accident” → table “view” เลือก view เพื่อทำ Dashboard


![alt text](Archive/image/pic27.png)


* หน้าตาของ Dashboard



![alt text](Archive/image/pic24.jpg)

visualization [link](https://lookerstudio.google.com/reporting/d6e96e3c-c20d-4e2d-80ed-66db2802f6c7/page/M5kzD)

เมื่อดำเนินการทุกอย่างของโปรเจคเสร็จเรียบร้อยแล้ว ควรจะต้องทำการปิด Docker Compose เพื่อเลี่ยงไม่ให้เกิดปัญหาพื้นที่การจัดเก็บข้อมูล
```sh
docker compose down
```


































