# Data-Management-System
Data Management System used to manage the claim retention processing on insurance companies 
the primary Modules :
1. Box Management
   - modules :
     * Create New Box
     * Search for information of Specific Box
     * Update Box => used to update box data
     * Delete Box used to delete box by passing the box number
     * import new boxes by bulk => pull-out sample sheet -> fill-out the sample sheet with valid information -> import (the process will be go forward many steps in system validation - database constraint)
     * Update Box Number By Bulk => pull-out sample sheet (it takes only box number - and what field i need to upate) -> import
     * delete boxes by bulk pull-out sample sheet with box numbers -> import
       ![image](https://github.com/user-attachments/assets/f1574c6f-7ff1-4f63-97c0-6b797c927d4a)
      ![image](https://github.com/user-attachments/assets/5c52fec5-2e57-435f-9d9c-37321d3669f9)
      ![image](https://github.com/user-attachments/assets/009bb82d-f799-4e42-b677-f9afa19888b1)
      ![image](https://github.com/user-attachments/assets/11754f46-5870-4804-b6aa-ab937737efd9)




2. Claim Segregation
   - modules  :
     * Adding New Claim-Code
     * serach for information about Claim Code
     * Update Claim Code
     * Delete Claim Code
     * Import Claim Code By Bulk => pull-out sample sheet -> fill out the valid data -> import  (the process will be go forward many steps in system validation - database constraint)
     * update claims by bulk => pulling out the sheet and just insert the claim code and what field needs to be updated (filling out all fields in case of updating at all)
     * delete claims by bulk => pulling out the sheet and then filling out the claim code that's needs to be deleted
       ![image](https://github.com/user-attachments/assets/fcf21058-0d57-4fc6-8bc9-d4fb0c652458)
       ![image](https://github.com/user-attachments/assets/9668275b-3428-4435-9017-3376a08547fc)
       ![image](https://github.com/user-attachments/assets/4a1b0f05-1251-471c-834b-f58e4d03940a)



3. claim retrieval :
   the functionionality for this module is to update the claims but for some fields and in case of batch id 
i.e the update will be on the batch (set of claims related to specific provider - client -med ...) level
      ![image](https://github.com/user-attachments/assets/832650d0-0b4e-48fb-9065-5b4ed83cc6e2)
4. reimbusement segregation (same steps for claim segregation but with ifferent fiels)
5. master data : this tab of modules used for data validation i.e instead the user will insert many fiels in different modules it will be drop down or search field to the fiels that's inside the database
   - designong : the master data management instance form normalized table i.e if we have field audit by user we have tabe on the data base called audit_by and master data instance from the primary table
   - modules :
     * master data : used to create new instance
     * update master data : used to update or delete the master data
       ![image](https://github.com/user-attachments/assets/aecada3f-9a96-4d42-8c81-d93f20ed20c0)
      Note : the Master data should be the first step when we aiming to create claims 

6. Insurance policy : Used to create new policy and it must to be the third step
    - modules :
      * insurance policy : moule for create new policy
      * all insurance policies : list o all created policies
      * update insurance plicy
      * delete insurance policy 
 ![image](https://github.com/user-attachments/assets/70f6dfe7-61b2-4044-a6aa-05069afff6b3)
7. reports : reports used in update box - claims status / kpi / data analysis
   the reports as follow :
      - claims per policy
      - claims per box
      - claims per batch
      - claims per request date
      - clais per insurance
      - box count per insurance and location
      - claims per date
      - claims per user 
