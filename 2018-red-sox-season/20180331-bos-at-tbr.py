import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-03-31
# https://www.baseball-reference.com/boxes/TBA/TBA201803310.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/03/31/529430/final

game = Scorecard(os.path.dirname(os.path.abspath(__file__)),
{
    "scorer": "Vicyorus",
    "date":   "2018-03-31 18:10-21:31",
    "at":     "Tropicana Field, St. Petersburg, FL",
    "att":    "17,838",
    "temp":   "72F, Dome",
    "wind":   "0mph, None",
    "away"   : {
        "team":    "Boston Red Sox",
        "starter": 22,
        "roster":  {
            # Lineup
            50 : "Mookie Betts",
            16 : "Andrew Benintendi",
            13 : "Hanley Ramirez",
            28 : "J.D. Martinez",
            2  : "Xander Bogaerts",
            18 : "Mitch Moreland",
            36 : "Eduardo Núñez",
            12 : "Brock Holt",
            3  : "Sandy León",

            # Starting pitcher
            22 : "Rick Porcello",

            # Bench
            11 : "Rafael Devers",
            23 : "Blake Swihart",
            19 : "Jackie Bradley Jr.",
            7  : "Christian Vázquez",

            # Bullpen
            39 : "Carson Smith",
            41 : "Chris Sale",
            61 : "Brian Johnson",
            66 : "Bobby Poyner",
            37 : "Heath Hembree",
            24 : "David Price",
            46 : "Craig Kimbrel",
            76 : "Hector Velázquez",
            64 : "Marcus Walden",
            56 : "Joe Kelly",
            32 : "Matt Barnes",
        },
        "lefties" : [
            41, 61, 66, 24
        ],
        "lineup" : [
            [50, "9"],
            [16, "8"],
            [13, "0"],
            [28, "7"],
            [2,  "6"],
            [18, "3"],
            [36, "5"],
            [12, "4"],
            [3,  "2"],
        ],
        "bench" : [
            [11, "3B"],
            [23, "C" ],
            [19, "CF"],
            [7,  "C" ],
        ],
        "bullpen" : [
            39, 41, 61, 66, 37, 24, 46, 76, 64, 56, 32
        ],
    },
    "home"   : {
        "team":    "Tampa Bay Rays",
        "starter": 36,
        "roster":  {
            # Lineup
            2  : "Denard Span",
            39 : "Kevin Kiermaier",
            27 : "Carlos Gómez",
            13 : "Brad Miller",
            5  : "Matt Duffy",
            18 : "Joey Wendle",
            11 : "Adeiny Hechavarría",
            0  : "Mallex Smith",
            45 : "Jesús Sucre",

            # Starting pitcher
            36 : "Andrew Kittredge",

            # Bench
            8  : "Rob Refsnyder",
            44 : "C.J. Cron",
            28 : "Daniel Robertson",
            40 : "Wilson Ramos",

            # Bullpen
            37 : "Alex Colomé",
            46 : "José Alvarado",
            48 : "Ryan Yarbrough",
            52 : "Chaz Roe",
            50 : "Austin Pruitt",
            34 : "Jake Faria",
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
            [11, "6"],
            [0,  "7"],
            [45, "2"],
        ],
        "bench" : [
            [8,  "LF"],
            [44, "1B"],
            [28, "SS"],
            [40, "C" ],
        ],
        "bullpen" : [
            37, 46, 48, 52, 50, 34, 4, 72, 35, 22, 54
        ],
    },
    "umpires" : {
        "HP" : "Andy Fletcher",
        "1B" : "Manny Gonzalez",
        "2B" : "Jeff Nelson",
        "3B" : "Laz Diaz",
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
# Pitching: TBR #36 Andrew Kittredge
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("c c b")
inn.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("b c b b f b")
inn.reach("BB")
inn.thrown_out(2, "13 DP6-4-3", 2, 36)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
inn.new_ab()
inn.pitch_list("b")
inn.out("DP6-4-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 1. TBR #2  Denard Span (X - X - X)
inn.new_ab()
inn.pitch_list("c b b")
inn.out("G6-3")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
inn.new_ab()
inn.pitch_list("b c b")
inn.out("L7")

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #36 Andrew Kittredge
inn = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("b b c b")
inn.hit(4, rbis=1)

# 6. BOS #18 Mitch Moreland (X - X - X)
inn.new_ab()
inn.pitch_list("c f b")
inn.out("F8")

# 7. BOS #36 Eduardo Núñez (X - X - X)
inn.new_ab()
inn.pitch_list("b c f b s")
inn.out("K")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 4. TBR #13 Brad Miller (X - X - X)
inn.new_ab()
inn.pitch_list("b b f c f c")
inn.out("!K")

# 5. TBR #5  Matt Duffy (X - X - X)
inn.new_ab()
inn.pitch_list("c c b b f f")
inn.out("F8")

# 6. TBR #18 Joey Wendle (X - X - X)
inn.new_ab()
inn.pitch_list("f f b c")
inn.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #36 Andrew Kittredge
inn = game.new_inning()

# 8. BOS #12 Brock Holt (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("F7")

# 9. BOS #3  Sandy León (X - X - X)
inn.new_ab()
inn.pitch_list("b c b b")
inn.out("L8")

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("c b c b")
inn.hit(2)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
inn.new_ab()
inn.pitch_list("c c f b 2 b f b")
inn.out("G4-3")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
inn.new_ab()
inn.pitch_list("b f f f")
inn.out("F8")

# 8. TBR #0  Mallex Smith (X - X - X)
inn.new_ab()
inn.pitch_list("f b b c b f")
inn.out("L8")

# 9. TBR #45 Jesús Sucre (X - X - X)
inn.new_ab()
inn.pitch_list("c c b b f f b b")
inn.reach("BB")
inn.advance(2, "2 1B")

# 1. TBR #2  Denard Span (X - X - 45)
inn.new_ab()
inn.hit(1)
inn.thrown_out(2, "39 FC6", 3, 22)

# 2. TBR #39 Kevin Kiermaier (X - 45 - 2)
inn.new_ab()
inn.pitch_list("c b")
inn.reach("FC6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #36 Andrew Kittredge
inn = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
inn.new_ab()
inn.pitch_list("b s")
inn.hit(2)
inn.advance(3, "18 SB")
inn.advance("U", "36 E5")

# 4. BOS #28 J.D. Martinez (X - 13 - X)
inn.new_ab()
inn.pitch_list("c b b f b")
inn.out("G6-3")

# Pitching change (TBR): #48 Ryan Yarbrough replaces #36 Andrew Kittredge
inn.pitching_substitution(48)

# 5. BOS #2  Xander Bogaerts (X - 13 - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("(F)P3")

# 6. BOS #18 Mitch Moreland (X - 13 - X)
inn.new_ab()
inn.pitch_list("b b f b f b")
inn.reach("BB")
inn.advance(2, "36 E5")

# 7. BOS #36 Eduardo Núñez (13 - X - 18)
inn.new_ab()
inn.pitch_list("b b 1")
inn.error(5)
inn.reach("E5")

# 8. BOS #12 Brock Holt (X - 18 - 36)
inn.new_ab()
inn.pitch_list("c f b f c")
inn.out("!K")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.pitch_list("b f f")
inn.out("F8")

# 4. TBR #13 Brad Miller (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("F8")

# 5. TBR #5  Matt Duffy (X - X - X)
inn.new_ab()
inn.pitch_list("f f b")
inn.hit(1)

# 6. TBR #18 Joey Wendle (X - X - 5)
inn.new_ab()
inn.pitch_list("b c b")
inn.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #48 Ryan Yarbrough
inn = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
inn.new_ab()
inn.out("F9")

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("b b b c c b")
inn.reach("BB")
inn.thrown_out(2, "13 FC6-4", 3, 48)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
inn.new_ab()
inn.pitch_list("c")
inn.reach("FC6-4")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("G5-3")

# 8. TBR #0  Mallex Smith (X - X - X)
inn.new_ab()
inn.hit(1)
inn.advance(2, "45 1B")

# 9. TBR #45 Jesús Sucre (X - X - 0)
inn.new_ab()
inn.pitch_list("1 1 1 f")
inn.hit(1)

# 1. TBR #2  Denard Span (X - 0 - 45)
inn.new_ab()
inn.pitch_list("c f s")
inn.out("K")

# 2. TBR #39 Kevin Kiermaier (X - 0 - 45)
inn.new_ab()
inn.pitch_list("f b s")
inn.out("(F)P5")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #48 Ryan Yarbrough
inn = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.hit(2)
inn.advance(4, "2 2B")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
inn.new_ab()
inn.pitch_list("b")
inn.hit(2, rbis=1)
inn.advance(3, "18 G3")

# 6. BOS #18 Mitch Moreland (X - 2 - X)
inn.new_ab()
inn.pitch_list("b f b")
inn.out("G3")

# 7. BOS #36 Eduardo Núñez (2 - X - X)
inn.new_ab()
inn.pitch_list("t f b")
inn.out("P5")

# 8. BOS #12 Brock Holt (2 - X - X)
inn.new_ab()
inn.pitch_list("b b f b b")
inn.reach("BB")

# 9. BOS #3  Sandy León (2 - X - 12)
inn.new_ab()
inn.pitch_list("c f b b f d s")
inn.out("K")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
inn = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.pitch_list("c b c")
inn.hit(2)
inn.advance(3, "5 1B")
inn.advance(4, "18 SF7")

# 4. TBR #13 Brad Miller (X - 27 - X)
inn.new_ab()
inn.pitch_list("f b f b c")
inn.out("!K")

# 5. TBR #5  Matt Duffy (X - 27 - X)
inn.new_ab()
inn.pitch_list("b f")
inn.hit(1)
inn.advance(2, "11 WP")

# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello
inn.pitching_substitution(37)

# 6. TBR #18 Joey Wendle (27 - X - 5)
inn.new_ab()
inn.pitch_list("f")
inn.out("SF7", rbis=1)

# 7. TBR #11 Adeiny Hechavarría (X - X - 5)
inn.new_ab()
inn.pitch_list("c f b b s")
inn.wp()
inn.out("K2-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #48 Ryan Yarbrough
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("L7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("c b c f b f s")
inn.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
inn.new_ab()
inn.pitch_list("t b f")
inn.out("P3")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
inn = game.new_inning()

# 8. TBR #0  Mallex Smith (X - X - X)
inn.new_ab()
inn.pitch_list("c b")
inn.out("L7")

# 9. TBR #45 Jesús Sucre (X - X - X)
inn.new_ab()
inn.pitch_list("b f c b s")
inn.out("K")

# 1. TBR #2  Denard Span (X - X - X)
inn.new_ab()
inn.pitch_list("b b b c c d")
inn.reach("BB")

# Pitching change (BOS): #66 Bobby Poyner replaces #37 Heath Hembree
inn.pitching_substitution(66)

# 2. TBR #39 Kevin Kiermaier (X - X - 2)
inn.new_ab()
inn.pitch_list("c b f f")
inn.out("P5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #48 Ryan Yarbrough
inn = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c b s f b")
inn.hit(1)
inn.advance(2, "2 1B")
inn.advance(3, "12 BB")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
inn.new_ab()
inn.pitch_list("b c 1")
inn.hit(1)
inn.advance(2, "12 BB")

# 6. BOS #18 Mitch Moreland (X - 28 - 2)
inn.new_ab()
inn.out("F8")

# Pitching change (TBR): #54 Sergio Romo replaces #48 Ryan Yarbrough
inn.pitching_substitution(54)

# 7. BOS #36 Eduardo Núñez (X - 28 - 2)
inn.new_ab()
inn.pitch_list("b b")
inn.out("F8")

# 8. BOS #12 Brock Holt (X - 28 - 2)
inn.new_ab()
inn.pitch_list("d b c f b b")
inn.reach("BB")

# 9. BOS #3  Sandy León (28 - 2 - 12)
inn.new_ab()
inn.pitch_list("c f b s")
inn.out("K")


# Bot 8th
# Pitching: BOS #66 Bobby Poyner
inn = game.new_inning()

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.hit(4, rbis=1)

# 4. TBR #13 Brad Miller (X - X - X)
inn.new_ab()
inn.pitch_list("b b")
inn.out("P3")

# Pitching change (BOS): #39 Carson Smith replaces #66 Bobby Poyner
inn.pitching_substitution(39)

# 5. TBR #5  Matt Duffy (X - X - X)
inn.new_ab()
inn.hit(1)
inn.advance(2, "11 SB")

# 6. TBR #18 Joey Wendle (X - X - 5)
inn.new_ab()
inn.pitch_list("b f c b f 1 1 s")
inn.out("K")

# 7. TBR #11 Adeiny Hechavarría (X - X - 5)
inn.new_ab()
inn.pitch_list("c 1 1 1 b s 1 d d")
inn.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #52 Chaz Roe
inn = game.new_inning()

# Pitching change (TBR): #52 Chaz Roe replaces #54 Sergio Romo
inn.pitching_substitution(52)

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b b c b b")
inn.reach("BB")
inn.thrown_out(2, "13 CS", 2, 52)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
inn.new_ab()
inn.pitch_list("1 1")
inn.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - 50)
inn.new_ab()
inn.pitch_list("1 c s b b b f")
inn.out("P2")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
inn = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #39 Carson Smith
inn.pitching_substitution(46)

# 8. TBR #0  Mallex Smith (X - X - X)
inn.new_ab()
inn.pitch_list("c s b b f b b")
inn.reach("BB")
inn.thrown_out(1, "44 DP6-3", 2, 46)

# Offensive change (TBR): Pinch-hitter #44 C.J. Cron replaces #45 Jesús Sucre, batting 9th
inn.offensive_substitution(9, 44, "PH")

# 9. TBR #44 C.J. Cron (X - X - 0)
inn.new_ab()
inn.pitch_list("1 d 1")
inn.out("DP6-3")

# 1. TBR #2  Denard Span (X - X - X)
inn.new_ab()
inn.pitch_list("b c c f f b")
inn.out("P6")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: TBR
# LP: TBR #36 Andrew Kittredge
game.losing_pitcher(36)

#print(game)
game.generate_scorecard()
