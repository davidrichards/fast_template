=========
Questions
=========

What are the core reasons to use tox?
What do I need at my fintertips to use tox?
What PEPs are involved with this tutorial?
Why split the source into subdomains?

Most projects don't need to have too much structure. Sometimes a project can get stuck in inertia--the size of the project makes every change too complicated and development slows down. When this occurs, it's probably a good idea to create a few subdomains.

The cost of this includes:...

Why split a project into so many layers?

Architecture develops an opinion about which parts of the system should be flexible, and which should be rigid. Flexibility often looks like easier to change. Rigidity looks like easier to test.

A domain that is database agnostic can speak to the actual language and work that people want to accomplish. Practice doing this without planning database tables, see how different it might look.

...

Where do the Docker configurations go?
How do I organize Docker containers?
How do I maintain system state in Docker? (setup, run DDL, ensure communication, etc.)
What different types of tests do you use?
How do you run the tests?
How do you develop clean internal dependencies?
Why use FastAPI?
What technologies work best with FastAPI?
How do I test-drive FastAPI?
