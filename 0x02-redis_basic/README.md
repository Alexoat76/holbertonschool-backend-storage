<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Redis-darkred.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x02. Redis basic

This project contains some tasks how to implement and use ***`redis`*** for basic operations.

<p align="center">
  <img width="380"  
        src="https://dwglogo.com/wp-content/uploads/2017/12/1100px_Redis_Logo_01-1024x707.png"
  >
</p>

# Getting Started :running:	
<div style="text-align: justify">

## Table of Contents
* [About](#about)
* [Resources](#resources-books)
* [Requirements](#requirements)
* [Files](#files-file_folder)
* [Tasks](#tasks)
* [Credits](#credits)

## About

- ***[Redis](https://intranet.hbtn.io/rltoken/U1qk6ej0LyzeD6PEjXJGlA)***


## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=redis&oq=redis&aqs=chrome..69i57j0i512l9.1821j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=REDIS)

- **[Redis commands](https://intranet.hbtn.io/rltoken/NBDXjPGhkwAPO7ovFw1ADA)** 
- **[Redis python client](https://intranet.hbtn.io/rltoken/2mB6Jt5nRoKHBpbLFaaZwA)** 
- **[How to Use Redis With Python](https://intranet.hbtn.io/rltoken/l1rtS7SsOH4-eA_bbA-Rww)** 
- **[Redis Crash Course Tutorial](https://intranet.hbtn.io/rltoken/U1qk6ej0LyzeD6PEjXJGlA)**

## Requirements
### General

- All files will be interpreted/compiled on *`Ubuntu 18.04 LTS`* using *`python3`* (version 3.7)
- All files should end with a new line
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The first line of all your files should be exactly  *` #!/usr/bin/env python3 `* 
- The code should use the  ` pycodestyle `  style (version 2.5)
- All modules should have documentation ( *` python3 -c 'print(__import__("my_module").__doc__)' `* )
- All classes should have documentation ( *` python3 -c 'print(__import__("my_module").MyClass.__doc__)' `* )
- All functions and methods should have documentation ( *` python3 -c 'print(__import__("my_module").my_function.__doc__)' `*  and  
	*` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' `* )
- A documentation is not a simple word, it???s a real sentence explaining what???s the purpose of the module, class or method (the length of it will be verified)
- All functions and coroutines must be type-annotated.

## More Info
## Install Redis on Ubuntu

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Use Redis in a container
Redis server is stopped by default - when you are starting a container, you should start it with: *` service redis-server start `* 

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-backend-storage.git`	
- Access to directory: `cd 0x02-redis_basic`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

### Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. *`Provided by Holberton School`*.
		
---

## Tasks

+ [x] 0\. **Writing strings to Redis**

+ **[exercise.py](./exercise.py)**

Create a   *` Cache `*   class. In the   *` __init__ `*   method, store an instance of the Redis client as a private variable named   *` _redis `*    (using   *` redis.Redis() `*  )   and flush the instance using *` flushdb `*. <br>

Create a   *` store `*   method that takes a   *` data `*   argument and returns a string. The method should generate a random key (e.g. using   *` uuid `*  ), store the input data in Redis using the random key and return the key. <br>

Type-annotate   *` store `*   correctly. Remember that   *` data `*   can be a   *` str `*,  *` bytes `*,  *` int `*  or  *` float `*.

```bash
$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
$ 
```
---

+ [x] 1\. **Reading from Redis and recovering original type**

+ **[exercise.py](./exercise.py)**

Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store   *` "a" `*   as a UTF-8 
	string, it will be returned as   *` b"a" `*   when retrieved from the server. <br>

In this exercise we will create a   *` get `*   method that take a   *` key `*   string argument and an optional   *` Callable `*   argument named   *` fn `*  . This callable will be used to convert the data back 
	to the desired format. <br>

Remember to conserve the original   *` Redis.get `*   behavior if the key does not exist. <br>

Also, implement 2 new methods:   *` get_str `*   and   *` get_int `*   that will automatically parametrize   *` Cache.get `*   with the correct conversion function. <br>

The following code should not raise:

```bash
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

```
---

+ [x] 2\. **Incrementing values**

+ **[exercise.py](./exercise.py)**

Familiarize yourself with the   *` INCR `*   command and its python equivalent. <br>

In this task, we will implement a system to count how many times methods of the   *` Cache `*   class are called. <br>

Above   *` Cache `*   define a   *` count_calls `*   decorator that takes a single   *` method `*   *` Callable `*   argument and returns a   *` Callable `*. <br>

As a key, use the qualified name of   *` method `*   using the   *` __qualname__ `*   dunder method. <br>

Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method. <br>

Remember that the first argument of the wrapped function will be   *` self `*   which is the instance itself, which lets you access the Redis instance. <br>

Protip: when defining a decorator it is useful to use   *` functool.wraps `*   to conserve the original function???s name, docstring, etc. Make sure you use it as described  **[here](https://intranet.hbtn.io/rltoken/-uqNijoWLQP46jI2hT1ZUw)**. <br>

Decorate   *` Cache.store `*   with   *` count_calls `*. <br>

```bash
$ cat main.py
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))

$ ./main.py
b'1'
b'3'
$ 
```
---

+ [x] 3\. **Storing lists**

+ **[exercise.py](./exercise.py)**

Familiarize yourself with redis commands   *` RPUSH `*  ,   *` LPUSH `*  ,   *` LRANGE `*  , etc. <br>

In this task, we will define a   *` call_history `*   decorator to store the history of inputs and outputs for a particular function. <br>

Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list. <br>

In   *` call_history `*  , use the decorated function???s qualified name and append   *` ":inputs" `*   and  * ` ":outputs" `*  to create input and output list keys, respectively. <br>

*` call_history `*   has a single parameter named   *` method `*   that is a   *` Callable `*   and returns a   *` Callable `*. <br>

In the new function that the decorator will return, use  *` rpush `*  to append the input arguments. Remember that Redis can only store strings, bytes and numbers. Therefore, 
	we can simply use   *` str(args) `*   to normalize. We can ignore potential   *` kwargs `*   for now. <br>

Execute the wrapped function to retrieve the output. Store the output using   *` rpush `*   in the   *` "...:outputs" `*   list, then return the output.
Decorate   *` Cache.store `*   with   *` call_history `*.

```bash
$ cat main.py
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

$ ./main.py
04f8dcaa-d354-4221-87f3-4923393a25ad
a160a8a8-06dc-4934-8e95-df0cb839644b
15a8fd87-1f55-4059-86aa-9d1a0d4f2aea
inputs: [b"('first',)", b"('secont',)", b"('third',)"]
outputs: ([b'04f8dcaa-d354-4221-87f3-4923393a25ad', 
	   b'a160a8a8-06dc-4934-8e95-df0cb839644b', 
	   b'15a8fd87-1f55-4059-86aa-9d1a0d4f2aea'])
$ 

```
---

+ [x] 4\. **Retrieving lists**

+ **[exercise.py](./exercise.py)**

In this tasks, we will implement a   *` replay `*   function to display the history of calls of a particular function.
Use keys generated in previous tasks to generate the following output:

```bash
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20

```
***Tip***: use   *` lrange `*   and   *` zip `*   to loop over inputs and outputs.

---

+ [x] 5\. **Implementing an expiring web cache and tracker**

+ **[web.py](./web.py)**

In this tasks, we will implement a   *` get_page `*   function (prototype:   *` def get_page(url: str) -> str: `*  ). The core of the function is very simple. It uses the   *` requests `*   module to obtain the HTML content of a particular URL and returns it. <br>

Start in a new file named   *` web.py `*   and do not reuse the code written in   *` exercise.py `*  . <br>

Inside   *` get_page `*   track how many times a particular URL was accessed in the key   *` "count:{url}" `*   and cache the result with an expiration time of 10 seconds. <br>

***Tip***: Use  *` http://slowwly.robertomurray.co.uk `*   to simulate a slow response and test your caching. <br>

***Bonus***: implement this use case with decorators.

---

## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Alex Orland Ar??valo Tribaldos`**  and credits for `group projects` are displayed in the respective `README.md` files.

<3915@holbertonstudents.com>
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Alexoat76)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/aoarevalot)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/Alexoat76/)

## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).
![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)
