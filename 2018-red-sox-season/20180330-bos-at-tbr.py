import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-03-30
# https://www.baseball-reference.com/boxes/TBA/TBA201803300.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/03/30/529421/final

game = Scorecard(os.path.dirname(os.path.abspath(__file__)),
{
    "scorer": "Vicyorus",
    "date":   "2018-03-30 19:10-21:56",
    "at":     "Tropicana Field, St. Petersburg, FL",
    "att":    "19,203",
    "temp":   "72F, Dome",
    "wind":   "0mph, None",
    "away"   : {
        "team":    "Boston Red Sox",
        "starter": 24,
        "roster":  {
            # Lineup
            50 : "Mookie Betts",
            16 : "Andrew Benintendi",
            13 : "Hanley Ramirez",
            28 : "J.D. Martinez",
            2  : "Xander Bogaerts",
            11 : "Rafael Devers",
            36 : "Eduardo Núñez",
            19 : "Jackie Bradley Jr.",
            7  : "Christian Vázquez",

            # Starting pitcher
            24 : "David Price",

            # Bench
            18 : "Mitch Moreland",
            12 : "Brock Holt",
            23 : "Blake Swihart",
            3  : "Sandy León",

            # Bullpen
            39 : "Carson Smith",
            22 : "Rick Porcello",
            41 : "Chris Sale",
            61 : "Brian Johnson",
            66 : "Bobby Poyner",
            37 : "Heath Hembree",
            46 : "Craig Kimbrel",
            76 : "Hector Velázquez",
            64 : "Marcus Walden",
            56 : "Joe Kelly",
            32 : "Matt Barnes",
        },
        "lefties" : [
            24, 41, 61, 66
        ],
        "lineup" : [
            [50, "9"],
            [16, "7"],
            [13, "3"],
            [28, "0"],
            [2,  "6"],
            [11, "5"],
            [36, "4"],
            [19, "8"],
            [7,  "2"],
        ],
        "bench" : [
            [18, "1B"],
            [12, "2B"],
            [23, "C" ],
            [3,  "C" ],
        ],
        "bullpen" : [
            39, 22, 41, 61, 66, 37, 46, 76, 64, 56, 32
        ],
    },
    "home"   : {
        "team":    "Tampa Bay Rays",
        "starter": 4,
        "roster":  {
            # Lineup
            5  : "Matt Duffy",
            39 : "Kevin Kiermaier",
            27 : "Carlos Gómez",
            44 : "C.J. Cron",
            40 : "Wilson Ramos",
            13 : "Brad Miller",
            11 : "Adeiny Hechavarría",
            28 : "Daniel Robertson",
            8  : "Rob Refsnyder",

            # Starting pitcher
            4  : "Blake Snell",

            # Bench
            2  : "Denard Span",
            18 : "Joey Wendle",
            0  : "Mallex Smith",
            45 : "Jesús Sucre",

            # Bullpen
            37 : "Alex Colomé",
            46 : "José Alvarado",
            48 : "Ryan Yarbrough",
            52 : "Chaz Roe",
            50 : "Austin Pruitt",
            36 : "Andrew Kittredge",
            34 : "Jake Faria",
            72 : "Yonny Chirinos",
            35 : "Matt Andriese",
            22 : "Chris Archer",
            54 : "Sergio Romo",
        },
        "lefties" : [
            4, 46, 48
        ],
        "lineup" : [
            [5,  "5"],
            [39, "8"],
            [27, "9"],
            [44, "0"],
            [40, "2"],
            [13, "3"],
            [11, "6"],
            [28, "4"],
            [8,  "7"],
        ],
        "bench" : [
            [2,  "CF"],
            [18, "2B"],
            [0,  "OF"],
            [45, "C" ],
        ],
        "bullpen" : [
            37, 46, 48, 52, 50, 36, 34, 72, 35, 22, 54
        ],
    },
    "umpires" : {
        "HP" : "Laz Diaz",
        "1B" : "Andy Fletcher",
        "2B" : "Manny Gonzalez",
        "3B" : "Jeff Nelson",
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
# Pitching: TBR #4  Blake Snell
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b b f b f")
inn.out("P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("b f c")
inn.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
inn.new_ab()
inn.pitch_list("c b b f f s")
inn.out("K")


# Bot 1st
# Pitching: BOS #24 David Price
inn = game.new_inning()

# 1. TBR #5  Matt Duffy (X - X - X)
inn.new_ab()
inn.pitch_list("c b b s")
inn.out("G3")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
inn.new_ab()
inn.pitch_list("b s")
inn.out("G1-3")

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.pitch_list("f c c")
inn.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #4  Blake Snell
inn = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("b b")
inn.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("F7")

# 6. BOS #11 Rafael Devers (X - X - X)
inn.new_ab()
inn.pitch_list("c s b b s")
inn.out("K")


# Bot 2nd
# Pitching: BOS #24 David Price
inn = game.new_inning()

# 4. TBR #44 C.J. Cron (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("P4")

# 5. TBR #40 Wilson Ramos (X - X - X)
inn.new_ab()
inn.out("F9")

# 6. TBR #13 Brad Miller (X - X - X)
inn.new_ab()
inn.pitch_list("b c b")
inn.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #4  Blake Snell
inn = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
inn.new_ab()
inn.pitch_list("s")
inn.out("P6")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
inn.new_ab()
inn.pitch_list("b s")
inn.out("G4-3")

# 9. BOS #7  Christian Vázquez (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.hit(1)
inn.thrown_out(2, "50 2-4", 3, 4)

# 1. BOS #50 Mookie Betts (X - X - 7)
inn.new_ab()
inn.pitch_list("c d")
inn.no_ab("2-4")


# Bot 3rd
# Pitching: BOS #24 David Price
inn = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
inn.new_ab()
inn.pitch_list("f b f b c")
inn.out("!K")

# 8. TBR #28 Daniel Robertson (X - X - X)
inn.new_ab()
inn.pitch_list("s")
inn.out("F7")

# 9. TBR #8  Rob Refsnyder (X - X - X)
inn.new_ab()
inn.pitch_list("b c b f s")
inn.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #4  Blake Snell
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b b")
inn.out("F7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("s b")
inn.out("G6-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
inn.new_ab()
inn.pitch_list("f b b")
inn.hit(1)
inn.advance(2, "28 BB")

# 4. BOS #28 J.D. Martinez (X - X - 13)
inn.new_ab()
inn.pitch_list("b b b c b")
inn.reach("BB")

# 5. BOS #2  Xander Bogaerts (X - 13 - 28)
inn.new_ab()
inn.pitch_list("b s")
inn.out("F7")


# Bot 4th
# Pitching: BOS #24 David Price
inn = game.new_inning()

# 1. TBR #5  Matt Duffy (X - X - X)
inn.new_ab()
inn.out("G5-3")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
inn.new_ab()
inn.pitch_list("c b f")
inn.hit(1)
inn.advance(2, "44 1B")

# 3. TBR #27 Carlos Gómez (X - X - 39)
inn.new_ab()
inn.out("P2")

# 4. TBR #44 C.J. Cron (X - X - 39)
inn.new_ab()
inn.pitch_list("b b b c")
inn.hit(1)

# 5. TBR #40 Wilson Ramos (X - 39 - 44)
inn.new_ab()
inn.pitch_list("c d c f")
inn.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #4  Blake Snell
inn = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
inn.new_ab()
inn.pitch_list("c b s f")
inn.out("L9")

# 7. BOS #36 Eduardo Núñez (X - X - X)
inn.new_ab()
inn.pitch_list("c b b f")
inn.out("G2-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
inn.new_ab()
inn.pitch_list("c s f b b b f")
inn.out("(F)P5")


# Bot 5th
# Pitching: BOS #24 David Price
inn = game.new_inning()

# 6. TBR #13 Brad Miller (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.hit(1)
inn.thrown_out(2, "11 FC5-4", 1, 24)

# 7. TBR #11 Adeiny Hechavarría (X - X - 13)
inn.new_ab()
inn.pitch_list("f s")
inn.reach("FC5-4")
inn.thrown_out(2, "28 DP6-4-3", 2, 24)

# 8. TBR #28 Daniel Robertson (X - X - 11)
inn.new_ab()
inn.pitch_list("c b")
inn.out("DP6-4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #4  Blake Snell
inn = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
inn.new_ab()
inn.pitch_list("f")
inn.out("F9")

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b c b b b")
inn.reach("BB")
inn.advance(3, "13 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
inn.new_ab()
inn.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - 50)
inn.new_ab()
inn.pitch_list("c b 1 1 f d 1 1")
inn.hit(1)

# Pitching change (TBR): #52 Chaz Roe replaces #4  Blake Snell
inn.pitching_substitution(52)

# 4. BOS #28 J.D. Martinez (50 - X - 13)
inn.new_ab()
inn.pitch_list("f b f f f b b c")
inn.out("!K")


# Bot 6th
# Pitching: BOS #24 David Price
inn = game.new_inning()

# 9. TBR #8  Rob Refsnyder (X - X - X)
inn.new_ab()
inn.pitch_list("s c c")
inn.out("!K")

# 1. TBR #5  Matt Duffy (X - X - X)
inn.new_ab()
inn.pitch_list("b b b c f c")
inn.out("!K")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
inn.new_ab()
inn.pitch_list("b f")
inn.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #52 Chaz Roe
inn = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("c f f")
inn.hit(2)
inn.advance(4, "11 1B")

# Pitching change (TBR): #46 José Alvarado replaces #52 Chaz Roe
inn.pitching_substitution(46)

# 6. BOS #11 Rafael Devers (X - 2 - X)
inn.new_ab()
inn.pitch_list("s s b")
inn.hit(1, rbis=1)
inn.advance(2, "36 1B")
inn.advance(3, "19 DP4-6-3")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
inn.new_ab()
inn.pitch_list("1 c")
inn.hit(1)
inn.thrown_out(2, "19 DP4-6-3", 1, 46)

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - 36)
inn.new_ab()
inn.pitch_list("b l c f d")
inn.out("DP4-6-3")

# 9. BOS #7  Christian Vázquez (11 - X - X)
inn.new_ab()
inn.pitch_list("b c f s")
inn.out("K2-3")


# Bot 7th
# Pitching: BOS #24 David Price
inn = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.pitch_list("f f")
inn.out("F8")

# 4. TBR #44 C.J. Cron (X - X - X)
inn.new_ab()
inn.pitch_list("b c")
inn.out("F8")

# 5. TBR #40 Wilson Ramos (X - X - X)
inn.new_ab()
inn.pitch_list("f")
inn.hit(1)

# 6. TBR #13 Brad Miller (X - X - 40)
inn.new_ab()
inn.pitch_list("f")
inn.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #35 Matt Andriese
inn = game.new_inning()

# Pitching change (TBR): #35 Matt Andriese replaces #46 José Alvarado
inn.pitching_substitution(35)

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("c b")
inn.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("b f b s f f f")
inn.out("(F)P5")

# 3. BOS #13 Hanley Ramirez (X - X - X)
inn.new_ab()
inn.pitch_list("f c f s")
inn.out("K")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
inn = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #24 David Price
inn.pitching_substitution(32)

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
inn.new_ab()
inn.pitch_list("f f b b f c")
inn.out("!K")

# Offensive change (TBR): Pinch-hitter #2 Denard Span replaces #28 Daniel Robertson, batting 8th
inn.offensive_substitution(8, 2, "PH")

# 8. TBR #2  Denard Span (X - X - X)
inn.new_ab()
inn.pitch_list("c s b b b b")
inn.reach("BB")

# Offensive change (TBR): Pinch-hitter #18 Joey Wendle replaces #8 Rob Refsnyder, batting 9th
inn.offensive_substitution(9, 18, "PH")

# 9. TBR #18 Joey Wendle (X - X - 2)
inn.new_ab()
inn.pitch_list("f b 1")
inn.out("L5")

# 1. TBR #5  Matt Duffy (X - X - 2)
inn.new_ab()
inn.pitch_list("b d")
inn.out("P3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #35 Matt Andriese
inn = game.new_inning()

# Defensive switch (TBR): #2 Denard Span moves to LF
inn.defensive_switch(2, "7")

# Defensive switch (TBR): #18 Joey Wendle moves to 2B
inn.defensive_switch(18, "4")

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c b f f")
inn.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.hit(2)
inn.advance(3, "11 G5-3")

# 6. BOS #11 Rafael Devers (X - 2 - X)
inn.new_ab()
inn.out("G5-3")

# 7. BOS #36 Eduardo Núñez (2 - X - X)
inn.new_ab()
inn.pitch_list("b s s s")
inn.out("K2-3")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
inn = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
inn.pitching_substitution(46)

# Defensive change (BOS): #18 Mitch Moreland replaces #13 Hanley Ramirez (1B), playing 1B, batting 3rd
inn.defensive_substitution(3, 18, "3")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
inn.new_ab()
inn.pitch_list("b c f s")
inn.out("K")

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.pitch_list("s f b f c")
inn.out("!K")

# 4. TBR #44 C.J. Cron (X - X - X)
inn.new_ab()
inn.pitch_list("c b s b b s")
inn.out("K")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: TBR
# LP: TBR #52 Chaz Roe
game.losing_pitcher(52)

#print(game)
game.generate_scorecard()
