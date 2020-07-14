# Kelsier project
*“There’s always another secret.”*
* [ ] Architecture overview required

## Modules
Represent connection between third-party application and core, or with some component, which can be used without this program.

### Microsoft TO-DO integration
* [x] Check ability to use API
* [x] Try to query task list with graph explorer https://developer.microsoft.com/en-us/graph/graph-explorer
* [x] Find example app to start
* [ ] Modify app to allow auth without web interface  
* [ ] Get rid of web deps (django and etc).  
     *Should I? It will be still kind of service, and access to web application can be useful for testing / maintenance.*
* [ ] Add functionality to get task from specific directory

On question:
* [ ] Mark task implemented. (Command like: Mark A task implemented)
### Telegram integration
* [ ] Find articles/tutorials/etc about telegram bot creation
* [ ] Create simple bot, which can get command for user and
### Instapaper or pocket integration
* [ ] Take a look at Instapaper API
* [ ] Take a look at Pocket API    
### Speech recognition
### Speech generator
### GUI/Web interface
* [ ] Think about using Web interface instead of telegram for first time

## Glue interfaces
Model-view representation? For different kind of request data will be different and view for modules too.

* [ ] Think how to represent requests data.

## Core
Potential container of trash code.
### CommandExtractor
* [ ] Extract from simple command what to do just using regex or smth like this
* [ ] Based on

On question:
* [ ] Improved command extractor using NLP
### PipelineCommander
? Is this a possible scenario, in which more than two modules will be involved?


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
