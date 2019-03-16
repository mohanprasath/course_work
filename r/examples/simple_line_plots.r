x = c(1:1000000)
y = c(1:1000000)


plot(x, y, "l", col="black")
lines(x, log(y), "l", col="green")
lines(x, 2*y, "l", col="blue")
title("simple x,y line plots")
# text(locator(), labels=c("x,y", "2x,y", "x, 2y"))