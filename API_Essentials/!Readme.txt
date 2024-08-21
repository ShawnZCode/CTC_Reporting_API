To leverage the Reporting API you will need to acquire your reporting key from CTC Software
Email: LicenseRequest@ctcsoftware.com
Subject: ReportingAPI Key Request

Excel:
1) Open the Excel File

2) Enable the External Content

3) Use the reporting API key you receive to update the ReportKey parmeter found at:
 Data -> Queries & Connections -> Parameters -> reportApiKey

4) In the Power Query Editor window navigate to File -> Optiona and settings -> Query Options
   a) In the Query Options window navigate to Pricavy, setting 'Privacy Levels' to 'Ignore the...' option
   b) OK this option

5) Use Home -> 'Close & Load' to close the Query Settings

6) Save the Excel File

7) Use Data -> Refresh All to refresh the base data

8) The first refresh will pop a message asking about Privacy Levels. Check 'Ignore All' for this file.

9) Allow the refresh to complete, then save the Excel file


Power BI:
1) Open the PowerBI file

2) In PowerBI Desktop use Home -> Transform Data -> Edit Parameters to update the full path to your XLSx file.

3) Save the PowerBI file

4) Use Home -> Refresh to refresh all of the data from the excel file

5) Save the PowerBI file and have fun navigating the data

FAQ:
1) My Excel data refresh is throwing permissions errors
   a) This is often due to company set permissions or not settings the permissions listed in the Excel steps
   b) Reach out to CTC Support at TechSupport@CTCSoftware.com with a screenshot of the error(s) you are getting

2) My Excel data refresh is throwing memory errors
   a) This is most commonly due to using Excel from the 32bit office installation.
      i) Only 64bit can process all of the data efficiently
   b) This may also happen if the number of daya you are requesting is feturning mote than the data storage
      abilities of Excel, even in 63bit
      i) try reducing the number of days you are requesting, or use the Query Settings to turn off some of the
         data you may not need immeadiatly. If the dataset is large enough, you may need to isolate each endpoint
         in a separate Excel file... Technically Excel is not a large format database, despite this process using
         it in that way.