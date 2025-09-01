1. Class Elements in Hotstar:-
Classes represent blueprints of entities in Hotstar.
Examples:
User (represents a Hotstar user)
Movie (represents a movie or show)
Subscription (represents subscription plans)
Player (represents video player)
RecommendationEngine (represents personalized suggestions)

2. Object Elements in Hotstar:-
Objects are real instances created from classes.
Examples:
user1 = User("Pravalika", "pravalika@gmail.com")
movie1 = Movie("Avengers: Endgame", "Action", 180)
sub1 = Subscription("Premium", 299)

3. Abstraction in Hotstar
Abstraction hides complex logic and shows only necessary details.
Examples:
PaymentGateway class hides how payment works (card/UPI/wallet).
Player class hides buffering, resolution handling, network issues.

4. Polymorphism in Hotstar:-
Polymorphism means same function behaves differently for different objects.
Examples:
play() method can play movies, series, or sports.
make_payment() method works differently for Card/UPI/Wallet.

5. Inheritance in Hotstar:-
Inheritance allows reusing code from parent classes.
Examples:
User → PremiumUser, FreeUser
Content → Movie, Series, LiveStream

6. Encapsulation in Hotstar:-
Encapsulation means data hiding + controlled access.
Examples:
Subscription details (plan validity, expiry date) should not be directly editable.
User password hidden and accessed only through getters/setters.


Classes:    User, Movie, Subscription, Player, RecommendationEngine
Objects:     user1, movie1, sub1
Abstraction: PaymentGateway, Player buffering
Polymorphism: play() works differently for Movie/LiveMatch
Inheritance:  User → PremiumUser/FreeUser
Encapsulation: private subscription details, password hiding