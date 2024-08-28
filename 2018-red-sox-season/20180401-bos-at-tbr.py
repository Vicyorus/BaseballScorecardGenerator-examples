import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-04-01
# https://www.baseball-reference.com/boxes/TBA/TBA201804010.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/04/01/529445/final

game = Scorecard(os.path.dirname(os.path.abspath(__file__)),
{
    "scorer": "Vicyorus",
    "date":   "2018-04-01 13:10-16:34",
    "at":     "Tropicana Field, St. Petersburg, FL",
    "att":    "14,256",
    "temp":   "72F, Dome",
    "wind":   "0mph, None",
    "away"   : {
        "team":    "Boston Red Sox",
        "starter": 76,
        "roster":  {
            # Lineup
            50 : "Mookie Betts",
            11 : "Rafael Devers",
            28 : "J.D. Martinez",
            2  : "Xander Bogaerts",
            18 : "Mitch Moreland",
            7  : "Christian Vázquez",
            19 : "Jackie Bradley Jr.",
            23 : "Blake Swihart",
            12 : "Brock Holt",

            # Starting pitcher
            76 : "Hector Velázquez",

            # Bench
            36 : "Eduardo Núñez",
            16 : "Andrew Benintendi",
            3  : "Sandy León",
            13 : "Hanley Ramirez",

            # Bullpen
            39 : "Carson Smith",
            22 : "Rick Porcello",
            41 : "Chris Sale",
            61 : "Brian Johnson",
            66 : "Bobby Poyner",
            37 : "Heath Hembree",
            24 : "David Price",
            46 : "Craig Kimbrel",
            64 : "Marcus Walden",
            56 : "Joe Kelly",
            32 : "Matt Barnes",
        },
        "lefties" : [
            41, 61, 66, 24
        ],
        "lineup" : [
            [50, "9"],
            [11, "5"],
            [28, "7"],
            [2,  "6"],
            [18, "3"],
            [7,  "2"],
            [19, "8"],
            [23, "0"],
            [12, "4"],
        ],
        "bench" : [
            [36, "SS"],
            [16, "LF"],
            [3,  "C" ],
            [13, "SS"],
        ],
        "bullpen" : [
            39, 22, 41, 61, 66, 37, 24, 46, 64, 56, 32
        ],
    },
    "home"   : {
        "team":    "Tampa Bay Rays",
        "starter": 34,
        "roster":  {
            # Lineup
            2  : "Denard Span",
            39 : "Kevin Kiermaier",
            27 : "Carlos Gómez",
            13 : "Brad Miller",
            5  : "Matt Duffy",
            18 : "Joey Wendle",
            40 : "Wilson Ramos",
            0  : "Mallex Smith",
            11 : "Adeiny Hechavarría",

            # Starting pitcher
            34 : "Jake Faria",

            # Bench
            8  : "Rob Refsnyder",
            44 : "C.J. Cron",
            28 : "Daniel Robertson",
            45 : "Jesús Sucre",

            # Bullpen
            37 : "Alex Colomé",
            46 : "José Alvarado",
            48 : "Ryan Yarbrough",
            52 : "Chaz Roe",
            50 : "Austin Pruitt",
            36 : "Andrew Kittredge",
            4  : "Blake Snell",
            72 : "Yonny Chirinos",
            35 : "Matt Andriese",
            22 : "Chris Archer",
            54 : "Sergio Romo",
        },
        "lefties" : [
            46, 48, 4
        ],
        "lineup" : [
            [2,  "0"],
            [39, "8"],
            [27, "9"],
            [13, "3"],
            [5,  "5"],
            [18, "4"],
            [40, "2"],
            [0,  "7"],
            [11, "6"],
        ],
        "bench" : [
            [8,  "LF"],
            [44, "1B"],
            [28, "SS"],
            [45, "C" ],
        ],
        "bullpen" : [
            37, 46, 48, 52, 50, 36, 4, 72, 35, 22, 54
        ],
    },
    "umpires" : {
        "HP" : "Manny Gonzalez",
        "1B" : "Jeff Nelson",
        "2B" : "Laz Diaz",
        "3B" : "Andy Fletcher",
    },
}
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: TBR #34 Jake Faria
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b c f b f f b")
t1.hit(1)
t1.advance(2, "28 SB")

# 2. BOS #11 Rafael Devers (X - X - 50)
t1.new_ab()
t1.pitch_list("c")
t1.out("F9")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t1.new_ab()
t1.pitch_list("b s f f b 1 d f c")
t1.out("!K")

# 4. BOS #2  Xander Bogaerts (X - 50 - X)
t1.new_ab()
t1.pitch_list("c s d")
t1.out("F9")


# Bot 1st
# Pitching: BOS #76 Hector Velázquez
b1 = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
b1.new_ab()
b1.pitch_list("c c b f f b")
b1.out("L7")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
b1.new_ab()
b1.out("F8")

# 3. TBR #27 Carlos Gómez (X - X - X)
b1.new_ab()
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #34 Jake Faria
t2 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.out("G4-3")

# 6. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("c b b")
t2.out("L9")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("b b c f b f b")
t2.reach("BB")
t2.advance(2, "23 SB")

# 8. BOS #23 Blake Swihart (X - X - 19)
t2.new_ab()
t2.pitch_list("c c b b d b")
t2.reach("BB")

# 9. BOS #12 Brock Holt (X - 19 - 23)
t2.new_ab()
t2.pitch_list("c d f")
t2.out("L7")


# Bot 2nd
# Pitching: BOS #76 Hector Velázquez
b2 = game.new_inning()

# 4. TBR #13 Brad Miller (X - X - X)
b2.new_ab()
b2.hit(4, rbis=1)

# 5. TBR #5  Matt Duffy (X - X - X)
b2.new_ab()
b2.hit(1)
b2.advance(2, "40 1B")

# 6. TBR #18 Joey Wendle (X - X - 5)
b2.new_ab()
b2.pitch_list("b")
b2.out("(F)P5")

# 7. TBR #40 Wilson Ramos (X - X - 5)
b2.new_ab()
b2.pitch_list("b s f")
b2.hit(1)
b2.thrown_out(2, "11 FC6-4", 3, 76)

# 8. TBR #0  Mallex Smith (X - 5 - 40)
b2.new_ab()
b2.pitch_list("f b s b f f f b")
b2.out("F7")

# 9. TBR #11 Adeiny Hechavarría (X - 5 - 40)
b2.new_ab()
b2.pitch_list("b f b b")
b2.reach("FC6-4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #34 Jake Faria
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.reach("HBP")
t3.thrown_out(2, "28 FC5-4", 2, 34)

# 2. BOS #11 Rafael Devers (X - X - 50)
t3.new_ab()
t3.pitch_list("t c s")
t3.out("K")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t3.new_ab()
t3.reach("FC5-4")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
t3.new_ab()
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #76 Hector Velázquez
b3 = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
b3.new_ab()
b3.pitch_list("b c f s")
b3.out("K")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 3. TBR #27 Carlos Gómez (X - X - X)
b3.new_ab()
b3.pitch_list("f f b t")
b3.out("KT")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #34 Jake Faria
t4 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b c f")
t4.out("G5-3")

# 6. BOS #7  Christian Vázquez (X - X - X)
t4.new_ab()
t4.pitch_list("s")
t4.out("L8")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("f b")
t4.error(1)
t4.reach("E1")
t4.advance(2, "23 1B")

# 8. BOS #23 Blake Swihart (X - X - 19)
t4.new_ab()
t4.pitch_list("b f")
t4.hit(1)

# 9. BOS #12 Brock Holt (X - 19 - 23)
t4.new_ab()
t4.pitch_list("d d f")
t4.out("G3-1")


# Bot 4th
# Pitching: BOS #76 Hector Velázquez
b4 = game.new_inning()

# 4. TBR #13 Brad Miller (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("F8")

# 5. TBR #5  Matt Duffy (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F7")

# 6. TBR #18 Joey Wendle (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.advance(2, "40 BB")

# 7. TBR #40 Wilson Ramos (X - X - 18)
b4.new_ab()
b4.pitch_list("b 1 f s b b f b")
b4.reach("BB")

# 8. TBR #0  Mallex Smith (X - 18 - 40)
b4.new_ab()
b4.pitch_list("f s b f f")
b4.out("L8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #34 Jake Faria
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.hit(1)
t5.advance(2, "11 BB")
t5.advance(4, "28 1B")

# 2. BOS #11 Rafael Devers (X - X - 50)
t5.new_ab()
t5.pitch_list("b c t 1 b f 1 b f b")
t5.reach("BB")
t5.advance(2, "28 1B")

# 3. BOS #28 J.D. Martinez (X - 50 - 11)
t5.new_ab()
t5.pitch_list("c f f")
t5.hit(1, rbis=1)

# Pitching change (TBR): #46 José Alvarado replaces #34 Jake Faria
t5.pitching_substitution(46)

# 4. BOS #2  Xander Bogaerts (X - 11 - 28)
t5.new_ab()
t5.pitch_list("c f f s")
t5.out("K")

# 5. BOS #18 Mitch Moreland (X - 11 - 28)
t5.new_ab()
t5.pitch_list("b 2 s c")
t5.out("F8")

# 6. BOS #7  Christian Vázquez (X - 11 - 28)
t5.new_ab()
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #76 Hector Velázquez
b5 = game.new_inning()

# 9. TBR #11 Adeiny Hechavarría (X - X - X)
b5.new_ab()
b5.out("L4")

# 1. TBR #2  Denard Span (X - X - X)
b5.new_ab()
b5.pitch_list("c s b")
b5.out("P5")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
b5.new_ab()
b5.pitch_list("f b s b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #46 José Alvarado
t6 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("b s b b f f f")
t6.hit(1)
t6.advance(2, "12 BB")
t6.advance(3, "50 HBP")
t6.advance(4, "11 1B")

# Pitching change (TBR): #72 Yonny Chirinos replaces #46 José Alvarado
t6.pitching_substitution(72)

# 8. BOS #23 Blake Swihart (X - X - 19)
t6.new_ab()
t6.pitch_list("f d f s")
t6.out("K")

# 9. BOS #12 Brock Holt (X - X - 19)
t6.new_ab()
t6.pitch_list("p c b b c b")
t6.reach("BB")
t6.advance(2, "50 HBP")
t6.thrown_out(4, "11 9-2", 2, 72)
t6.advance(3, "11 1B")

# 1. BOS #50 Mookie Betts (X - 19 - 12)
t6.new_ab()
t6.pitch_list("c f")
t6.reach("HBP")
t6.advance(2, "11 9-2")

# 2. BOS #11 Rafael Devers (19 - 12 - 50)
t6.new_ab()
t6.pitch_list("f d s")
t6.hit(1, rbis=1)

# 3. BOS #28 J.D. Martinez (X - 50 - 11)
t6.new_ab()
t6.pitch_list("s s")
t6.out("L7")


# Bot 6th
# Pitching: BOS #76 Hector Velázquez
b6 = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
b6.new_ab()
b6.out("G5-3")

# 4. TBR #13 Brad Miller (X - X - X)
b6.new_ab()
b6.pitch_list("f c b s")
b6.out("K")

# 5. TBR #5  Matt Duffy (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.hit(1)
b6.advance(3, "18 2B")

# Pitching change (BOS): #64 Marcus Walden replaces #76 Hector Velázquez
b6.pitching_substitution(64)

# 6. TBR #18 Joey Wendle (X - X - 5)
b6.new_ab()
b6.pitch_list("f")
b6.hit(2)

# 7. TBR #40 Wilson Ramos (5 - 18 - X)
b6.new_ab()
b6.pitch_list("s")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #72 Yonny Chirinos
t7 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.out("G5-3")

# 5. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("c f f b f")
t7.out("G5-3")

# 6. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.reach("HBP")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 7)
t7.new_ab()
t7.pitch_list("b b s")
t7.out("F7")


# Bot 7th
# Pitching: BOS #64 Marcus Walden
b7 = game.new_inning()

# 8. TBR #0  Mallex Smith (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("L6")

# 9. TBR #11 Adeiny Hechavarría (X - X - X)
b7.new_ab()
b7.pitch_list("b b c")
b7.out("L1")

# 1. TBR #2  Denard Span (X - X - X)
b7.new_ab()
b7.pitch_list("f c b")
b7.out("G3-1")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #72 Yonny Chirinos
t8 = game.new_inning()

# 8. BOS #23 Blake Swihart (X - X - X)
t8.new_ab()
t8.out("F7")

# 9. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("c b b c f b f")
t8.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("G5-3")


# Bot 8th
# Pitching: BOS #66 Bobby Poyner
b8 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #64 Marcus Walden
b8.pitching_substitution(66)

# 2. TBR #39 Kevin Kiermaier (X - X - X)
b8.new_ab()
b8.out("F7")

# Pitching change (BOS): #32 Matt Barnes replaces #66 Bobby Poyner
b8.pitching_substitution(32)

# 3. TBR #27 Carlos Gómez (X - X - X)
b8.new_ab()
b8.pitch_list("b s l b s")
b8.out("K")

# 4. TBR #13 Brad Miller (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")

# 5. TBR #5  Matt Duffy (X - X - 13)
b8.new_ab()
b8.pitch_list("c f b f f c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #72 Yonny Chirinos
t9 = game.new_inning()

# 2. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("s f c")
t9.out("!K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("s f b s")
t9.out("K")


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
b9.pitching_substitution(56)

# Defensive change (BOS): #16 Andrew Benintendi replaces #28 J.D. Martinez (LF), playing LF, batting 3rd
b9.defensive_substitution(3, 16, "7")

# 6. TBR #18 Joey Wendle (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("P5")

# 7. TBR #40 Wilson Ramos (X - X - X)
b9.new_ab()
b9.pitch_list("s s b c")
b9.out("!K")

# 8. TBR #0  Mallex Smith (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.hit(1)
b9.advance(3, "11 1B")

# 9. TBR #11 Adeiny Hechavarría (X - X - 0)
b9.new_ab()
b9.pitch_list("b 1 1 s c f")
b9.hit(1)

# 1. TBR #2  Denard Span (0 - X - 11)
b9.new_ab()
b9.pitch_list("c b 1 b f b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #76 Hector Velázquez
game.winning_pitcher(76, is_away_team=True)
# SV: BOS #56 Joe Kelly
game.save_pitcher(56, is_away_team=True)

# Loser team: TBR
# LP: TBR #46 José Alvarado
game.losing_pitcher(46)

#print(game)
game.generate_scorecard()
