
housing = read.csv("C:/Users/ricci/Desktop/Projects/FRED/Data.csv", header = TRUE)
View(housing)
View(housing)
myvars = c("GOOG", "YAHOO", "WEED")
Housing2 = housing[myvars]
 
View(Housing2)
results <- lm(GOOG ~ YAHOO + WEED, data=Housing2)
summary(results)$r.squared

results <- lm(WEED ~ YAHOO + GOOG, data=Housing2)
summary(results)$r.squared
summary(results)$r.squared

models <- mtcars %>%
+     split(.$cyl) %>%
+     map(function(df) lm(mpg ~ wt + hp, data = df))
for(v in models) print(summary(v)$r.squared)

models %>%
  map(summary) %>%
  map_dbl(~.$r.squared)+

models <- mtcars %>%
     split(.$cyl) %>%
     map(function(df) lm(mpg ~ wt + drat +wt+qsec, data = df))
m

for (var in names(trans)) {
    mtcars[[var]] <- trans[[var]](mtcars[[var]])
}

models <- mtcars %>%
+     split(.$cyl) %>%
+     map(function(df) lm(mpg ~ wt, data = df))
