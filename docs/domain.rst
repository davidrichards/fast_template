======
Domain
======

The domain is meant to be a storage-agnostic representation of the data and the interactions with the data. Writing a domain is a bit of an art. My process involves:

* Start on paper.
* Name the first entities that come to mind.
* Draw arrows between the dependencies.
* Put labels on the arrows, how one entity interacts with another.
* Play games with synonyms, ensure I've found good names, not just the first names that came to mind.
* Identify the aggregates, how more than one entity is grouped together. These can overlap, meaning more than one aggregate can contain the same entity.
* Look for short cuts on attributes, where value objects can simplify the domain.

Once you have that, it's time to code it up. I like to use dataclasses, but they need a little coaxing:

* Use `__post_init__` to validate the data. Use value objects here.
* Define `__eq__` and `__hash__` to make the dataclasses hashable. This is important for sets and dictionaries. It simplifies the code in the service layer as well.
* Add `serialize` and `deserialize` methods to convert to and from dictionaries. This is important for the service layer. I've included some utility functions that work with dicts, JSON, and Avro.
