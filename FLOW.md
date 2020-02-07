# Railway Flow
The goal of this document is to explain how railway manages communication between stations and how you can use this to build and run your own train application.

## Terminology
- *Railway*:
- *Central*:
- *Master*:
- *Station*:
- *Train*:


## Master and Station applications
Railway distinguishes the Master and Station part of the application. 
But both need to be packaged in the same repository. 
Based on the train/task configuration the Station java application will trigger "runMaster.sh" or "runStation.sh".