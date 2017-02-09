#Unit Testing

Good Source - http://stackoverflow.com/questions/2665812/what-is-mocking

##Mocking

```Mocking is primarily used in unit testing. An object under test may have dependencies on other (complex) objects. To isolate the behaviour of the object you want to test you replace the other objects by mocks that simulate the behavior of the real objects. This is useful if the real objects are impractical to incorporate into the unit test.```

Ex. object.expects(:expected_method).at_least_once

##Stubbing

You can force a method to return what YOU want

Ex. ```Namespace(Maybe)::SomeClass.stubs(:shop_ids).returns(@shop_ids) where @shop_ids I make as [1,2,3]```

The original class method is thus overwritten by the stub's value
