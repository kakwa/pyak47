Roadmap
=======

Short term
**********

* code reorganization for better reusability
* a command line client to manage a pool of benchers
* the command line client must support an interactive mode, and a not interactive mode
* the command line methods must be available as a library (a bench could be launch by an external mean)
* a true daemonizable server mode
* handling listening on multiple interfaces
* one daemon managing several available jobs
* one bench == one new process to prevent memory leaks over time.

Mid term
********

* ascii graph output (could be usefull if use inside an IRC bot for example)
* authentification and confidentiality between the client and the benchers
* shared objects (to share some resources between jobs and reduce memory footprint)

