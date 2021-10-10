
## Initialize

```shell
  mkdir Coordinates-Location
  cd Coordinates-Location
```

## North - Coordinates

```shell  
  mkdir North
  cd North

    touch NDegree.txt
    x=`echo "(5 * 5) - (4 * 2 * 2)" | bc -l`
    y=`echo "°" `
    echo $x$y >> NDegree.txt

    touch NMinutes.txt
    a=`echo "5" `
    b=`echo "‘" `
    echo $a$b >> NMinutes.txt 

    touch NSeconds.txt
    c=`echo "38+0.1 " | bc`
    d=`echo "’’" `
    echo $c$d >> NSeconds.txt

    touch NorthCoordinate.txt 
    cat NDegree.txt NMinutes.txt NSeconds.txt | { tr -d '\n'; echo; } > NorthCoordinate.txt 
    cp NorthCoordinate.txt ../
    rm NorthCoordinate.txt 

cd ..
mv NorthCoordinate.txt North.txt

```

## East - Coordinates

```shell  
  mkdir East
  cd East

    touch EDegree.txt
    a=`echo "76" `
    b=`echo "°" `
    echo $a$b >> EDegree.txt

    touch EMinutes.txt
    a=`echo "29" `
    b=`echo "‘" `
    echo $a$b >> EMinutes.txt 

    touch ESeconds.txt
    a=`echo "30" `
    b=`echo "’’" `
    echo $a$b >> ESeconds.txt

    touch EastCoordinate.txt 
    cat EDegree.txt EMinutes.txt ESeconds.txt | { tr -d '\n'; echo; } > EastCoordinate.txt 
    cp EastCoordinate.txt ../
    rm EastCoordinate.txt 

cd ..
mv EastCoordinate.txt East.txt

```

## Final Formatting

```bash
    cat North.txt East.txt > Location-Coordinate.txt
    nano Location-Coordinate.txt
```

#### Output : 
### 9°5‘38.1“N 76°29‘30“E


### Location
![Location](Screenshot.png)
