# frederick-tech-hackathon-2022-fire-rescue
Data Analytics For Frederick County Fire And Rescue

## Software Requirements for Frederick Fire and Rescue Project
TechFrederick Hackathon 2022
Project Owner: Chris Dunn
Email: cdunn@frederickcountymd.gov

### Purpose
The function of Quality Assurance in Emergency Medical Services is a rapidly developing field.  The use of data analytics to monitor trends in patient types, patient care, and system needs is of particular interest.  The Maryland Institute for Emergency Medical Services System (MIEMSS) is the regulatory and licensing agency in the State of Maryland for Emergency Medical Services.  MIEMSS has contracted with software company Imagetrend, as the required program used by EMS providers, to complete electronic patient care reports (ePCR) for each patient encounter.  Within the Imagetrend software “Elite,” a tool named “Report Writer” exists that allows Quality Assurance Officers to mine data out of the ePCR’s that EMS providers complete.  This tool allows data to be extracted from the database of ePCR’s, and exported to .pdf or .csv file type.  These data reports can be automated, on a scheduled basis, to be delivered via email to a desired receiver. While the Report Writer tool is customizable to produce data reports, it is limited in its data analytics and visualization capacity.  Currently, the data reports being created have to be manually entered into existing spreadsheets to be used by more advanced data analytics programs.  The request is the development of software that will be able to extract the .csv or .pdf files out of the user’s Outlook inbox and update or replace existing Excel Spreadsheets that can be linked and referenced by Microsoft Power BI for expanded data analytics capability.

### Intended Audience
The intended user for the software will be the Quality Assurance Officer and other EMS Management Officers within Frederick County Division of Fire Rescue Services responsible for maintaining dashboards of information to monitor trends within Emergency Medical Services.

### Intended Use
Currently the Quality Assurance Officer is responsible for transferring the data that is produced by Report Writer into Excel Spreadsheets which are linked to dashboards within Microsoft Power Business Intelligence (BI).  These dashboards provide Division management with data visualization tools and graphs providing meaningful information about the calls EMS units are running.  Relying on the manual data entry by the Quality Assurance Officer to provide this service represents a single point of failure and vulnerability.  The desire is to design a software that will automate this process of transferring data from an inbox to Excel.  Additionally, some of the data reports that are generated capture time specific information.  Simply overwriting an existing file is not always a desirable solution.  For example, Imagetrend produces a daily report, at 06:00 hours, of patient care reports that have not been created for the previous 24 hours.  While those reports are eventually created, one of the data points tracked is the daily count of missing reports at shift change (06:00).  After those reports are eventually created, they are no longer “missing,” and therefore can’t be identified by Report Writer. The spreadsheet that tracks that count requires new entries into the existing sheet daily, as opposed to overwriting the existing sheet with a daily count.  This manual data entry is both time consuming, subject to human error, and presents a vulnerability to the Division as a single point of failure.

### Scope
The goal of this software is to automate the process of data entry.  The personnel assigned as the Quality Assurance Officer changes on a 2 year rotation with a steep learning curve.  Removing the component of manual data entry and software proficiency minimizes the vulnerability of the Division in monitoring the quality of EMS care being provided to citizens.  As the Division of Fire Rescue continually strives to provide the highest quality of service to the citizens of Frederick County, automating this process will be a process improvement for the management of the Division.

### Assumptions and Dependencies
What assumptions are you making that could cause an error in your approach? Is the project reliant on any other factors that could affect the development of the software?
Frederick County’s Interagency Information Technology (IIT) Division provides support to the Division of Fire Rescue as a division of Frederick County Government.  The network, computers, and software used by the Division of Fire Rescue Services are subject to the rules and regulations of Frederick County IIT.  As such, there may be network security protocols, firewalls, or other obstacles in place set by IIT which may complicate implementation.  Similarly, the software may be subject to the approval of IIT management for use on the county system.

### Requirements
Take time to define the functional requirements that are essential for the software to be built.
The software must be able to automate the process of saving a .csv or .pdf file sent to an Outlook Inbox, add information to an existing Excel Spreadsheet or overwrite an existing Excel Spreadsheet on a network drive, using the existing file name so that Microsoft Power BI can pull the data out of that spreadsheet to develop data visualizations.  This process needs to be able to be turned on and off, but must also occur without prompting when active.  The process can occur either at a scheduled time or be triggered by keywords in the email.  The software must be able to be analyzed by Frederick County IIT staff to ensure security compliance.


### Build
`pyinstaller --distpath src --onefile --additional-hooks-dir=. -w cli.py`

Make sure cli.spec looks like this:
```
...
    datas=[
        (
            "{$PYTHON_ENV}/Lib/site-packages/streamlit/static",
            "./streamlit/static"
        )
    ],
...
```

`pyinstaller --distpath src cli.spec`