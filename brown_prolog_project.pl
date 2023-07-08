servesAll(american,[salad,steak,sandwiches,burgers,fried_chicken]).
servesAll(burger_place,[burgers,fries,onion_rings]).
servesAll(chinese,[eggrolls,rice,shrimp,soup,noodles]).
servesAll(indian,[papadam,bagan_bharta,rice,tandoori,naan]).
servesAll(italian,[salad,pasta,cioppino,snapper,bread,garlic_bread]).
servesAll(japanese,[sashimi,rice,tempura,noodles]).
servesAll(mediterranean,[gyros,hummus,pita,falafel]).
servesAll(mexican,[tacos,beans,rice,enchiladas,fish_tacos]).
servesAll(pizza_place,[pizza,salad,garlic_bread]).
servesAll(thai,[rice,noodles,larb,pad_thai]).

serves(Kind, Dish) :-
    servesAll(Kind,Dishes),
    member(Dish, Dishes).

allDishes(vegetarian,[beans,bagan_bharta,enchiladas,falafel,hummus,pizza,salad,soup,tempura,onion_rings,naan,papadam,bread,rice,noodles,pita,garlic_bread,pasta,fries]).
allDishes(meat,[burgers,enchiladas,gyros,pad_thai,pizza,steak,sandwiches,fried_chicken,tacos,tandoori,larb]).
allDishes(seafood,[snapper,cioppino,sashimi,shrimp,clams,fish_tacos,tempura]).
allDishes(starch,[naan,papadam,bread,rice,noodles,pita,garlic_bread,pasta,fries]).

dish(Type,Dish) :-
    allDishes(Type,Dishes),
    member(Dish,Dishes).

allCuisines(american,[waterman_grille,red_stripe]).
allCuisines(burger_place,[shake_shack]).
allCuisines(chinese,[yans,chinatown]).
allCuisines(indian,[kabob_n_curry]).
allCuisines(italian,[pasta_beach,al_forno]).
allCuisines(japanese,[haruki]).
allCuisines(mediterranean,[andreas,east_side_pockets]).
allCuisines(mexican,[bajas,dolores,tallulahs]).
allCuisines(pizza_place,[pizza_marvin,mikes]).
allCuisines(thai,[heng,bees,lims]).

cuisine(Kind, Restaurant) :-
    allCuisines(Kind, Restaurants),
    member(Restaurant, Restaurants).

allLocations(fox_point,[pizza_marvin,dolores,tallulahs,bees,al_forno]).
allLocations(thayer_street,[yans,bajas,andreas,chinatown,kabob_n_curry,heng,mikes,east_side_pockets,shake_shack]).
allLocations(wayland,[waterman_grille,red_stripe,pasta_beach,haruki,lims]).

location(Location, Restaurant) :-
    allLocations(Location, Restaurants),
    member(Restaurant, Restaurants).

allMenuItems(waterman_grille,[salad,steak,sandwiches,burgers,fried_chicken]).
allMenuItems(red_stripe,[salad,steak,sandwiches,burgers,fried_chicken]).
allMenuItems(shake_shack,[burgers,fries,onion_rings]).
allMenuItems(yans,[eggrolls,rice,shrimp,soup,noodles]).
allMenuItems(chinatown,[eggrolls,rice,shrimp,soup,noodles]).
allMenuItems(kabob_n_curry,[papadam,bagan_bharta,rice,tandoori,naan]).
allMenuItems(pasta_beach,[salad,pasta,cioppino,snapper,bread,garlic_bread]).
allMenuItems(al_forno,[salad,pasta,cioppino,snapper,bread,garlic_bread]).
allMenuItems(haruki,[sashimi,rice,tempura,noodles]).
allMenuItems(andreas,[gyros,hummus,pita,falafel]).
allMenuItems(east_side_pockets,[gyros,hummus,pita,falafel]).
allMenuItems(bajas,[tacos,beans,rice,enchiladas,fish_tacos]).
allMenuItems(dolores,[tacos,beans,rice,enchiladas,fish_tacos]).
allMenuItems(tallulahs,[tacos,beans,rice,enchiladas,fish_tacos]).
allMenuItems(pizza_marvin,[pizza,salad,garlic_bread]).
allMenuItems(mikes,[pizza,salad,garlic_bread]).
allMenuItems(heng,[rice,noodles,larb,pad_thai]).
allMenuItems(bees,[rice,noodles,larb,pad_thai]).
allMenuItems(lims,[rice,noodles,larb,pad_thai]).

menuitems(Restaurant, Food) :-
    allMenuItems(Restaurant, Foods),
    member(Food, Foods).

allCuisinesinArea(fox_point,[pizza_place,mexican,mexican,thai,italian]).
allCuisinesinArea(thayer_street,[thai,mexican,mediterranean,chinese,indian,thai,pizza_place,mediterranean,burger_place]).
allCuisinesinArea(wayland,[american,american,italian,japanese,thai]).

cuisineinarea(Location, Cuisine) :-
    allCuisinesinArea(Location, Cuisines),
    member(Cuisine,Cuisines).




