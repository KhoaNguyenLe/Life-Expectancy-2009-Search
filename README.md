## Environment setup

In the terminal you'll need to install any Python libraries you want to use. You'll almost certainly want to use the `pymongo` library. To install it, go to the terminal in Codespaces and type the following.

```
pip install pymongo
```

[Doumentation for PyMongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)

## Importing the data

Using the file `import.py` you're going to import the JSON file into a database named `data` into a collection called `life_expectency`. 

The data you're given has more than we want to deal with, so the `import.py` file is going to strip out only what we care about an insert it into the MongoDB database.

Run the following in the terminal.

```
python import.py
```

**Full File**
```json
"data": [
        [
            "row-7ecr-rw5c.zdsg",
            "00000000-0000-0000-5A87-4B7286C42576",
            0,
            1662041970,
            null,
            1662041970,
            null,
            "{ }",
            "Alabama",
            "Total",
            "73.2",
            "0.067",
            "71.9 - 75.3"
        ],
        [
            "row-c82q_65bd~4m7u",
            "00000000-0000-0000-3E6F-9C71E3FDC33B",
            0,
            1662041970,
            null,
            1662041970,
            null,
            "{ }",
            "Alaska",
            "Total",
            "76.6",
            "0.176",
            "75.4 - 76.8"
        ],
```

What actually needs to get inserted are the following two dictionaries. Notice that life expectency - `le` in the dictionary - is a string in JSON but needs to be a float in the database. 

```json
[{
    "state": "Alabama",
    "gender": "Total",
    "le": 73.2
}, 
{ 
    "state": "Alaska",
    "gender": "Total",
    "le": 76.6
},
// Other states
]
```

### find_state_overall

Returns the life expectency of the state specified for all genders. That's where `gender == "Total"`.

### find_state_male

Same as above, but only considers `gender == "Male"`

### find_state_female

Same again, but this time for `gender == "Female"`

### find_highest

Returns the state and life expectency, in that order, as a tuple of the state with the highest life expectency that matches `gender`. `gender` will always be `Total`, `Male` or `Female`. 

The return value should be a tuple like `("Idaho", 75.5)`

### find_lowest

Same as above, but returns the lowest life expectency.

### find_average

Returns the average life expectency for all states matching `gender`. 


