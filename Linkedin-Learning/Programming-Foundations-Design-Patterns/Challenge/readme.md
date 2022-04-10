### Challenge

<details>
    <summary><strong>Design Patterns Quiz</strong></summary>
    <strong>The original creators of design patterns were known as the gang of four. How many design patterns are there?</strong>
    <br>
    23
    <br>
    <br>
    <strong>Design patterns are about reusing and the design experience. How is the design pattern expressed?</strong>
    <br>
    It is expressed by a definition, a class diagram, and collected into a catalog of patterns.
    <br>
    <br>
    <strong>Design patterns are comprised of object-oriented basics. What are the object-oriented basics</strong>
    <br>
    The basics are inheritance, polymorphism, abstraction, and encapsulation.
</details>
<details>
    <summary><strong>The Strategy Pattern Quiz</strong></summary>
    <strong>An object is an instance of a class. What is a concrete instance when working with design patterns?</strong>
    <br>
    A concrete instance refers to any occurrence of objects that exist during the runtime of a computer program.
    <br>
    <br>
    <strong>Which coding format "implements" when deriving a superclass with a subclass?</strong>
    <br>

```
public class SomeSubClass implements SomeSuperClass {
   public void doSomething() {     System.out.println("Using implements to derive classes");
   }
}
```
<br>
    <br>
    <strong>Design patterns use algorithms for the strategy pattern. How is the strategy pattern defined</strong>
    <br>
    The strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
    <br>
    <br>
    <strong>Which difference does the HAS-A relationship have in comparison to the IS-A relationship?</strong>
    <br>
    Instead of inheriting behavior like the IS-A relationship, the HAS-A composes the behavior.
    <br>
    <br>
    <strong>When working with inheritance, which kind of relationship do you have with classes?</strong>
    <br>
    Classes share an IS-A relationship.
    <br>
    <br>
    <strong>What does abstract mean in inheritance when working with subclasses?</strong>
    <br>
    Subclasses must override all abstract methods of its abstract superclass.
    <br>
    <br>
    <strong>What is an interface, and how is it used in design patterns?</strong>
    <br>
    Design patterns use interfaces to define methods an object must have to be considered a particular type.
    <br>
    <br>
    <strong>When working with design principles, which of the following defines "Encapsulate What Varies"?</strong>
    <br>
    Once you separate the parts that are changing, you can then modify those parts without affecting the rest of the code.
</details>
<details>
    <summary><strong>The Adapter Pattern Quiz</strong></summary>
    <strong>The Adapter pattern is a software design pattern. Which coding format is correct for creating the Adapter pattern?</strong>
    <br>

```
class BirdAdapter implements ToyDuck
{
    Bird bird;
    public BirdAdapter(Bird bird)
    {
         this.bird = bird;
    }
}
```
<br>
    <br>
    <strong>Design patterns use the Adapter pattern to solve problems with different interface problems. Which action does the Adapter pattern take?</strong>
    <br>
    The Adapter pattern handles the work of translating the request to a new class.
</details>
<details>
    <summary><strong>The Observer Pattern Quiz</strong></summary>
    <strong>The Observer pattern has design principles of loose coupling. Describe the term "loose coupling."</strong>
    <br>
    Loosely coupled means routines are called by an application and executed as needed.
    <br>
    <br>
    <strong>The Observer pattern has two components; they are the subscriber and the publisher. Which type of relationship exists with the subscriber and publisher?</strong>
    <br>
    Publishers post messages to a message broker, and subscribers register subscriptions to the message broker.
    <br>
    <br>
    <strong>The Observer pattern uses the Subject interface. Which three methods comprise the Subject interface?</strong>
    <br>
    RegisterObserver method, RemoveObserver method, and NotifyObserver method
    <br>
    <br>
    <strong>Why are the subjects and observers in the Observer pattern considered "loosely coupled"?</strong>
    <br>
    Because they do not know a lot about each other, they are independent.
</details>
<details>
    <summary><strong>The Decorator Pattern Quiz</strong></summary>
    <strong>In Design Patterns, we favor composition over inheritance. Why is this beneficial?</strong>
    <br>
    We can use composition to get the flexibility, without all the complexity that inheritance gives us.
    <br>
    <br>
    <strong>Why is the "open-closed principle" so important in the Decorator pattern?</strong>
    <br>
    The open-closed principle explains that classes should be open for extension, but closed for modification.
</details>
<details>
    <summary><strong>The Iterator Pattern Quiz</strong></summary>
    <strong>Java provides several collections to store objects in a data structure. Which interface is used to empty or store more items in a collection?</strong>
    <br>
    The iterator interface allows data to be accessed, removed, or stored in a collection.
    <br>
    <br>
    <strong>Java has a variety of different collections. What is the difference between Array and an ArrayList?</strong>
    <br>
    The Array is a collection of data types, whereas the ArrayList is a collection of objects.
    <br>
    <br>
    <strong>Java has several packages that contain interfaces and classes, which you can use for the Iterator pattern. Which package can be used for the Iterator pattern?</strong>
    <br>
    Java has the "java.util.iterator" package for the Iterator pattern.
    <br>
    <br>
    <strong>The Iterator pattern is used frequently. Which coding format creates the Iterator pattern?</strong>
    <br>

```
var animalIterator = animals.makeIterator()
while let animal = animalIterator.next() {
     print(animal)
}
```
</details>
<details>
    <summary><strong>The Factory Pattern Quiz</strong></summary>
    <strong>The Factory Pattern also has a Simple Factory Pattern. What is the Simple Factory Pattern?</strong>
    <br>
    The Simple Factory Pattern decouples the process of creating and using objects from the clients.
    <br>
    <br>
    <strong>Why does the Factory pattern provide loose coupling and high cohesion?</strong>
    <br>
    The Factory pattern encapsulates object creation logic, which makes it easy to change later.
    <br>
    <br>
    <strong>With the Factory Method pattern, which process is implemented with the abstract superclass "PizzaStore," and derived down to the subclasses "PizzaStores"?</strong>
    <br>
    Every algorithm is used by the subclasses from the superclass.
</details>