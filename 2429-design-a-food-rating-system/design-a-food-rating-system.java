import java.util.*;

class FoodRatings {
    private Map<String, String> foodToCuisine;

    private Map<String, Integer> foodToRating;

    private Map<String, PriorityQueue<Food>> cuisineToFoods;

    private static class Food {
        String name;
        int rating;

        Food(String name, int rating) {
            this.name = name;
            this.rating = rating;
        }
    }

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        foodToCuisine = new HashMap<>();
        foodToRating = new HashMap<>();
        cuisineToFoods = new HashMap<>();

        for (int i = 0; i < foods.length; i++) {
            String food = foods[i];
            String cuisine = cuisines[i];
            int rating = ratings[i];

            foodToCuisine.put(food, cuisine);
            foodToRating.put(food, rating);

            cuisineToFoods.putIfAbsent(cuisine, new PriorityQueue<>(
                (a, b) -> a.rating == b.rating ? a.name.compareTo(b.name) : b.rating - a.rating
            ));
            cuisineToFoods.get(cuisine).offer(new Food(food, rating));
        }
    }

    public void changeRating(String food, int newRating) {
        String cuisine = foodToCuisine.get(food);
        foodToRating.put(food, newRating);
        cuisineToFoods.get(cuisine).offer(new Food(food, newRating));
    }

    public String highestRated(String cuisine) {
        PriorityQueue<Food> pq = cuisineToFoods.get(cuisine);

        while (!pq.isEmpty()) {
            Food top = pq.peek();
            if (foodToRating.get(top.name) == top.rating) {
                return top.name;
            }
            pq.poll();
        }

        return "";
    }
}

