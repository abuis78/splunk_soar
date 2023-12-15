<h1>SPLUNK SOAR</h1>
In this repo you will find a small collection of playbooks, custom functions and apps that I developed during my project.

<h1>Disclaimer</h1>
Everything that is offered here as a download can be used at your own risk. I assume no liability and no guarantee. I will also not always keep these playbooks, custom functions and apps up to date. If you are missing something, please contact me and we will surely find a solution.

<h1>Playbooks</h1>
The playbooks are mostly structured in such a way that I try to follow a certain name conversion.

Example, phishing use_case:
phishing_<name>

Since I am following the concept of playbook reutilisation, playbooks that can also be used in other use cases are as follows in the name conversion. 

Example:
rc_input_<name>
rc_auto_<name>

All these playbooks are self-contained and will have input and output whereby all these playbooks will always have an output which can then be further processed in the parent playbook. (only applies to input playbooks)
