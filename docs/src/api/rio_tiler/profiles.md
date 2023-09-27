# Module rio_tiler.profiles

Image file profiles.

None

## Variables

```python3
img_profiles
```

## Classes

### ImagesProfiles

```python3
class ImagesProfiles(
    
)
```

#### Ancestors (in MRO)

* collections.UserDict
* collections.abc.MutableMapping
* collections.abc.Mapping
* collections.abc.Collection
* collections.abc.Sized
* collections.abc.Iterable
* collections.abc.Container

#### Static methods

    
#### fromkeys

```python3
def fromkeys(
    iterable,
    value=None
)
```

    

#### Methods

    
#### clear

```python3
def clear(
    self
)
```

    
D.clear() -> None.  Remove all items from D.

    
#### copy

```python3
def copy(
    self
)
```

    

    
#### get

```python3
def get(
    self,
    key,
    default=None
)
```

    
Like normal item access but return a copy of the key.

    
#### items

```python3
def items(
    self
)
```

    
D.items() -> a set-like object providing a view on D's items

    
#### keys

```python3
def keys(
    self
)
```

    
D.keys() -> a set-like object providing a view on D's keys

    
#### pop

```python3
def pop(
    self,
    key,
    default=<object object at 0x104315160>
)
```

    
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If key is not found, d is returned if given, otherwise KeyError is raised.

    
#### popitem

```python3
def popitem(
    self
)
```

    
D.popitem() -> (k, v), remove and return some (key, value) pair

as a 2-tuple; but raise KeyError if D is empty.

    
#### setdefault

```python3
def setdefault(
    self,
    key,
    default=None
)
```

    
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

    
#### update

```python3
def update(
    self,
    other=(),
    /,
    **kwds
)
```

    
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.

If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v

    
#### values

```python3
def values(
    self
)
```

    
D.values() -> an object providing a view on D's values

### JPEGProfile

```python3
class JPEGProfile(
    data={},
    **kwds
)
```

#### Ancestors (in MRO)

* rasterio.profiles.Profile
* collections.UserDict
* collections.abc.MutableMapping
* collections.abc.Mapping
* collections.abc.Collection
* collections.abc.Sized
* collections.abc.Iterable
* collections.abc.Container

#### Class variables

```python3
defaults
```

#### Static methods

    
#### fromkeys

```python3
def fromkeys(
    iterable,
    value=None
)
```

    

#### Methods

    
#### clear

```python3
def clear(
    self
)
```

    
D.clear() -> None.  Remove all items from D.

    
#### copy

```python3
def copy(
    self
)
```

    

    
#### get

```python3
def get(
    self,
    key,
    default=None
)
```

    
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

    
#### items

```python3
def items(
    self
)
```

    
D.items() -> a set-like object providing a view on D's items

    
#### keys

```python3
def keys(
    self
)
```

    
D.keys() -> a set-like object providing a view on D's keys

    
#### pop

```python3
def pop(
    self,
    key,
    default=<object object at 0x104315160>
)
```

    
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If key is not found, d is returned if given, otherwise KeyError is raised.

    
#### popitem

```python3
def popitem(
    self
)
```

    
D.popitem() -> (k, v), remove and return some (key, value) pair

as a 2-tuple; but raise KeyError if D is empty.

    
#### setdefault

```python3
def setdefault(
    self,
    key,
    default=None
)
```

    
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

    
#### update

```python3
def update(
    self,
    other=(),
    /,
    **kwds
)
```

    
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.

If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v

    
#### values

```python3
def values(
    self
)
```

    
D.values() -> an object providing a view on D's values

### PNGProfile

```python3
class PNGProfile(
    data={},
    **kwds
)
```

#### Ancestors (in MRO)

* rasterio.profiles.Profile
* collections.UserDict
* collections.abc.MutableMapping
* collections.abc.Mapping
* collections.abc.Collection
* collections.abc.Sized
* collections.abc.Iterable
* collections.abc.Container

#### Class variables

```python3
defaults
```

#### Static methods

    
#### fromkeys

```python3
def fromkeys(
    iterable,
    value=None
)
```

    

#### Methods

    
#### clear

```python3
def clear(
    self
)
```

    
D.clear() -> None.  Remove all items from D.

    
#### copy

```python3
def copy(
    self
)
```

    

    
#### get

```python3
def get(
    self,
    key,
    default=None
)
```

    
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

    
#### items

```python3
def items(
    self
)
```

    
D.items() -> a set-like object providing a view on D's items

    
#### keys

```python3
def keys(
    self
)
```

    
D.keys() -> a set-like object providing a view on D's keys

    
#### pop

```python3
def pop(
    self,
    key,
    default=<object object at 0x104315160>
)
```

    
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If key is not found, d is returned if given, otherwise KeyError is raised.

    
#### popitem

```python3
def popitem(
    self
)
```

    
D.popitem() -> (k, v), remove and return some (key, value) pair

as a 2-tuple; but raise KeyError if D is empty.

    
#### setdefault

```python3
def setdefault(
    self,
    key,
    default=None
)
```

    
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

    
#### update

```python3
def update(
    self,
    other=(),
    /,
    **kwds
)
```

    
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.

If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v

    
#### values

```python3
def values(
    self
)
```

    
D.values() -> an object providing a view on D's values

### PNGRAWProfile

```python3
class PNGRAWProfile(
    data={},
    **kwds
)
```

#### Ancestors (in MRO)

* rasterio.profiles.Profile
* collections.UserDict
* collections.abc.MutableMapping
* collections.abc.Mapping
* collections.abc.Collection
* collections.abc.Sized
* collections.abc.Iterable
* collections.abc.Container

#### Class variables

```python3
defaults
```

#### Static methods

    
#### fromkeys

```python3
def fromkeys(
    iterable,
    value=None
)
```

    

#### Methods

    
#### clear

```python3
def clear(
    self
)
```

    
D.clear() -> None.  Remove all items from D.

    
#### copy

```python3
def copy(
    self
)
```

    

    
#### get

```python3
def get(
    self,
    key,
    default=None
)
```

    
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

    
#### items

```python3
def items(
    self
)
```

    
D.items() -> a set-like object providing a view on D's items

    
#### keys

```python3
def keys(
    self
)
```

    
D.keys() -> a set-like object providing a view on D's keys

    
#### pop

```python3
def pop(
    self,
    key,
    default=<object object at 0x104315160>
)
```

    
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If key is not found, d is returned if given, otherwise KeyError is raised.

    
#### popitem

```python3
def popitem(
    self
)
```

    
D.popitem() -> (k, v), remove and return some (key, value) pair

as a 2-tuple; but raise KeyError if D is empty.

    
#### setdefault

```python3
def setdefault(
    self,
    key,
    default=None
)
```

    
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

    
#### update

```python3
def update(
    self,
    other=(),
    /,
    **kwds
)
```

    
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.

If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v

    
#### values

```python3
def values(
    self
)
```

    
D.values() -> an object providing a view on D's values

### WEBPProfile

```python3
class WEBPProfile(
    data={},
    **kwds
)
```

#### Ancestors (in MRO)

* rasterio.profiles.Profile
* collections.UserDict
* collections.abc.MutableMapping
* collections.abc.Mapping
* collections.abc.Collection
* collections.abc.Sized
* collections.abc.Iterable
* collections.abc.Container

#### Class variables

```python3
defaults
```

#### Static methods

    
#### fromkeys

```python3
def fromkeys(
    iterable,
    value=None
)
```

    

#### Methods

    
#### clear

```python3
def clear(
    self
)
```

    
D.clear() -> None.  Remove all items from D.

    
#### copy

```python3
def copy(
    self
)
```

    

    
#### get

```python3
def get(
    self,
    key,
    default=None
)
```

    
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

    
#### items

```python3
def items(
    self
)
```

    
D.items() -> a set-like object providing a view on D's items

    
#### keys

```python3
def keys(
    self
)
```

    
D.keys() -> a set-like object providing a view on D's keys

    
#### pop

```python3
def pop(
    self,
    key,
    default=<object object at 0x104315160>
)
```

    
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If key is not found, d is returned if given, otherwise KeyError is raised.

    
#### popitem

```python3
def popitem(
    self
)
```

    
D.popitem() -> (k, v), remove and return some (key, value) pair

as a 2-tuple; but raise KeyError if D is empty.

    
#### setdefault

```python3
def setdefault(
    self,
    key,
    default=None
)
```

    
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

    
#### update

```python3
def update(
    self,
    other=(),
    /,
    **kwds
)
```

    
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.

If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v

    
#### values

```python3
def values(
    self
)
```

    
D.values() -> an object providing a view on D's values