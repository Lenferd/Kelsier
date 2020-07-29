# Kelsier project
*“There’s always another secret.”*
* [ ] Architecture overview required

------------------
## Modules
Represent connection between third-party application and core, or with some component, which can be used without this program.

### Microsoft TO-DO integration
* https://docs.microsoft.com/en-us/azure/active-directory/develop/microsoft-graph-intro
* https://developer.microsoft.com/en-us/graph/graph-explorer
* Found sample application, which use Django as backend
* Used sample to create native application
* Added ability to get task folder url (id)
* Added ability to create a new task
* Task can be created in specific list using provided name of list 

Not important:
* [ ] Mark task implemented. (Command like: Mark A task implemented)
* [ ] Ability to get and print task 
* [ ] Ability to close specific task

### OneNote integration
* Can get page from OneNote
* [ ] Investigate, how "Fill form" functionality can be implemented. Like, I have template for every, and using telegram bot can ask myself questions from this template, and insert answers in specific fields.

### Telegram integration
* https://github.com/eternnoir/pyTelegramBotAPI
* Command are redirected to command extractor

Minor:
* [ ] Improve fault tolerance

### Reader integration
* Instapapper will not provide application token for any user.
* Pocket provide ability to get token without additional checks
* [ ] Auth using application to Pocket
### Speech recognition
### Speech generator
### GUI/Web interface
* [ ] Think about using Web interface instead of telegram for first time

------------------
## Glue interfaces
Model-view representation? For different kind of request data will be different and view for modules too.

* [ ] Think how to represent requests data.

------------------
## Core
Potential container of trash code.

* [ ] Add logger class
### Command Extractor
Try to understand user command, extract key phrases, run specific scenario.
* [ ] Extract from simple command what to do just using regex or smth like this
* [ ] Based on

On question:
* [ ] Improved command extractor using NLP

### Scenario Commander
To work with complex scenario

------------------
## Use case
### Ask film/serial to watch from list.
Command: Telegram: "What to watch?"  
Sequence:   
-> Modules::Telegram { Get user input }  
-> Core::CommandExtractor { Extract command. Need to get "TODO::Watch" object of task type }  
-> Glue::TODO { Ask for list of all Watch tasks}   
-> Modules::TODO { Request Watch list of task }  
-> Glue::TODO { Get random one, or based on additional criterion }  
Result: Film/serial <task desc>. Will see?  
TODO: Simplify this shit.  

### Fill daily task
Command : Telegram: "Plan day"  
Details: Plan 3 important work / non-work task, which should be completed today  
Sequence:   
-> Telegram { User input }  
-> Command Extractor { Create scenario pipeline }  
-> TODO: Add tasks
Result: Microsoft TO-DO will contain specified tasks in "My day" category.  

### Fill form (Day retrospective)
Command : Telegram: "Day retrospective"  
Sequence:  
-> Telegram { Get user input }  
-> Command Extractor { Understand, that some complex logic should be executed }  
-> OneNote: { Try to find template, create pipeline based on template }  
Result: Sequence of questions on Telegram side, answers are stored in OneNote
