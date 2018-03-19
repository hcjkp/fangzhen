s=tf('s');
g1=(2/(s+2))*((1/(1+0.2*s))*(0.33+0.67/(1+10*s)));
g2=200/(s/100 + 1)^2;
g3=-200/(s/100 + 1)^2 + (2000*s*((27*s)/5 + 1)*((21*s)/1000 + 1))/((3*s + 1)*(10*s + 1)*(s/100 + 1)*((47*s)/1000 + 1));
t=0:0.002:1;
c=step(g3,t);
plot(t,c); grid;
xlabel('t--sec'), ylabel('c(t)');
