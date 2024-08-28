import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TBR, 2018-03-29
# https://www.baseball-reference.com/boxes/TBA/TBA201803290.shtml
# https://www.mlb.com/gameday/red-sox-vs-rays/2018/03/29/529406/final

game = Scorecard(os.path.dirname(os.path.abspath(__file__)),
{
    "scorer": "Vicyorus",
    "date":   "2018-03-29 16:00-19:00",
    "at":     "Tropicana Field, St. Petersburg, FL",
    "att":    "31,042",
    "temp":   "72F, Dome",
    "wind":   "0mph, None",
    "away"   : {
        "team":    "Boston Red Sox",
        "starter": 41,
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
            41 : "Chris Sale",

            # Bench
            18 : "Mitch Moreland",
            12 : "Brock Holt",
            23 : "Blake Swihart",
            3  : "Sandy León",

            # Bullpen
            39 : "Carson Smith",
            22 : "Rick Porcello",
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
            39, 22, 61, 66, 37, 24, 46, 76, 64, 56, 32
        ],
    },
    "home"   : {
        "team":    "Tampa Bay Rays",
        "starter": 22,
        "roster":  {
            # Lineup
            5  : "Matt Duffy",
            39 : "Kevin Kiermaier",
            27 : "Carlos Gómez",
            44 : "C.J. Cron",
            40 : "Wilson Ramos",
            2  : "Denard Span",
            11 : "Adeiny Hechavarría",
            28 : "Daniel Robertson",
            8  : "Rob Refsnyder",

            # Starting pitcher
            22 : "Chris Archer",

            # Bench
            13 : "Brad Miller",
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
            4  : "Blake Snell",
            72 : "Yonny Chirinos",
            35 : "Matt Andriese",
            54 : "Sergio Romo",
        },
        "lefties" : [
            46, 48, 4
        ],
        "lineup" : [
            [5,  "5"],
            [39, "8"],
            [27, "9"],
            [44, "3"],
            [40, "2"],
            [2,  "7"],
            [11, "6"],
            [28, "4"],
            [8,  "0"],
        ],
        "bench" : [
            [13, "DH"],
            [18, "2B"],
            [0,  "OF"],
            [45, "C" ],
        ],
        "bullpen" : [
            37, 46, 48, 52, 50, 36, 34, 4, 72, 35, 54
        ],
    },
    "umpires" : {
        "HP" : "Jeff Nelson",
        "1B" : "Laz Diaz",
        "2B" : "Andy Fletcher",
        "3B" : "Manny Gonzalez",
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
# Pitching: TBR #22 Chris Archer
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("c f")
inn.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
inn.new_ab()
inn.pitch_list("f b s f b f b s")
inn.out("K")


# Bot 1st
# Pitching: BOS #41 Chris Sale
inn = game.new_inning()

# 1. TBR #5  Matt Duffy (X - X - X)
inn.new_ab()
inn.pitch_list("c c b b f s")
inn.out("K")

# 2. TBR #39 Kevin Kiermaier (X - X - X)
inn.new_ab()
inn.pitch_list("b c f s")
inn.out("K")

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.pitch_list("f b")
inn.out("P6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TBR #22 Chris Archer
inn = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("b s b b f d")
inn.reach("BB")
inn.advance(3, "2 2B")
inn.advance(4, "11 G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
inn.new_ab()
inn.pitch_list("b f b")
inn.hit(2)
inn.advance(3, "11 G6-3")
inn.advance(4, "36 HR")

# 6. BOS #11 Rafael Devers (28 - 2 - X)
inn.new_ab()
inn.pitch_list("b s f b")
inn.out("G6-3", rbis=1)

# 7. BOS #36 Eduardo Núñez (2 - X - X)
inn.new_ab()
inn.hit(4, rbis=2)

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
inn.new_ab()
inn.out("P6")

# 9. BOS #7  Christian Vázquez (X - X - X)
inn.new_ab()
inn.pitch_list("b c f b")
inn.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 7)
inn.new_ab()
inn.pitch_list("f f b d")
inn.out("(F)P3")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
inn = game.new_inning()

# 4. TBR #44 C.J. Cron (X - X - X)
inn.new_ab()
inn.pitch_list("b c f s")
inn.out("K")

# 5. TBR #40 Wilson Ramos (X - X - X)
inn.new_ab()
inn.pitch_list("c b")
inn.out("G6-3")

# 6. TBR #2  Denard Span (X - X - X)
inn.new_ab()
inn.pitch_list("f b b b c b")
inn.reach("BB")
inn.advance(2, "11 1B")
inn.advance(3, "28 PB")

# 7. TBR #11 Adeiny Hechavarría (X - X - 2)
inn.new_ab()
inn.pitch_list("b b")
inn.hit(1)
inn.advance(2, "28 PB")

# 8. TBR #28 Daniel Robertson (X - 2 - 11)
inn.new_ab()
inn.pitch_list("c b c b f c")
inn.pb()
inn.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TBR #22 Chris Archer
inn = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.out("P3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
inn.new_ab()
inn.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("c b s s")
inn.out("K")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
inn = game.new_inning()

# 9. TBR #8  Rob Refsnyder (X - X - X)
inn.new_ab()
inn.pitch_list("c b b b b")
inn.reach("BB")

# 1. TBR #5  Matt Duffy (X - X - 8)
inn.new_ab()
inn.pitch_list("b b")
inn.out("F8")

# 2. TBR #39 Kevin Kiermaier (X - X - 8)
inn.new_ab()
inn.pitch_list("b f b f f b s")
inn.out("K")

# 3. TBR #27 Carlos Gómez (X - X - 8)
inn.new_ab()
inn.pitch_list("b s f f b")
inn.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TBR #22 Chris Archer
inn = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("c f f f b")
inn.hit(1)
inn.thrown_out(2, "11 DP9-3", 2, 22)

# 6. BOS #11 Rafael Devers (X - X - 2)
inn.new_ab()
inn.pitch_list("b b")
inn.out("DP9-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
inn.new_ab()
inn.pitch_list("c f s")
inn.out("K")


# Bot 4th
# Pitching: BOS #41 Chris Sale
inn = game.new_inning()

# 4. TBR #44 C.J. Cron (X - X - X)
inn.new_ab()
inn.pitch_list("b f f b s")
inn.out("K")

# 5. TBR #40 Wilson Ramos (X - X - X)
inn.new_ab()
inn.pitch_list("c b")
inn.out("L8")

# 6. TBR #2  Denard Span (X - X - X)
inn.new_ab()
inn.out("L6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TBR #22 Chris Archer
inn = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
inn.new_ab()
inn.out("G3")

# 9. BOS #7  Christian Vázquez (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("b c b c s")
inn.out("K")


# Bot 5th
# Pitching: BOS #41 Chris Sale
inn = game.new_inning()

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
inn.new_ab()
inn.pitch_list("b s")
inn.out("G5-3")

# 8. TBR #28 Daniel Robertson (X - X - X)
inn.new_ab()
inn.pitch_list("c s s")
inn.out("K")

# 9. TBR #8  Rob Refsnyder (X - X - X)
inn.new_ab()
inn.pitch_list("f b b s b b")
inn.reach("BB")

# 1. TBR #5  Matt Duffy (X - X - 8)
inn.new_ab()
inn.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TBR #22 Chris Archer
inn = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
inn.new_ab()
inn.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
inn.new_ab()
inn.pitch_list("c b s b s")
inn.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
inn.new_ab()
inn.pitch_list("s b s f c")
inn.out("!K")


# Bot 6th
# Pitching: BOS #41 Chris Sale
inn = game.new_inning()

# 2. TBR #39 Kevin Kiermaier (X - X - X)
inn.new_ab()
inn.pitch_list("c b")
inn.out("G6-3")

# 3. TBR #27 Carlos Gómez (X - X - X)
inn.new_ab()
inn.pitch_list("s c b s")
inn.out("K")

# 4. TBR #44 C.J. Cron (X - X - X)
inn.new_ab()
inn.pitch_list("c s b b b f s")
inn.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TBR #22 Chris Archer
inn = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("f f")
inn.hit(2)
inn.advance(4, "11 2B")

# 6. BOS #11 Rafael Devers (X - 2 - X)
inn.new_ab()
inn.hit(2, rbis=1)

# Pitching change (TBR): #50 Austin Pruitt replaces #22 Chris Archer
inn.pitching_substitution(50)

# 7. BOS #36 Eduardo Núñez (X - 11 - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("G6-3")

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - X)
inn.new_ab()
inn.pitch_list("b c")
inn.out("P5")

# 9. BOS #7  Christian Vázquez (X - 11 - X)
inn.new_ab()
inn.out("G6-3")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
inn = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #41 Chris Sale
inn.pitching_substitution(32)

# 5. TBR #40 Wilson Ramos (X - X - X)
inn.new_ab()
inn.pitch_list("c")
inn.out("G5-3")

# 6. TBR #2  Denard Span (X - X - X)
inn.new_ab()
inn.pitch_list("c b c b")
inn.out("L9")

# 7. TBR #11 Adeiny Hechavarría (X - X - X)
inn.new_ab()
inn.pitch_list("c b f f b")
inn.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TBR #50 Austin Pruitt
inn = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
inn.new_ab()
inn.pitch_list("c c")
inn.hit(1)
inn.thrown_out(2, "13 2-3", 2, 50)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
inn.new_ab()
inn.pitch_list("c 1 b 1 b b f f")
inn.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - 50)
inn.new_ab()
inn.pitch_list("b f 1 f d b f b")
inn.reach("BB")
inn.thrown_out(2, "28 FC5-4", 3, 50)

# 4. BOS #28 J.D. Martinez (X - X - 13)
inn.new_ab()
inn.pitch_list("s s")
inn.reach("FC5-4")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
inn = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
inn.pitching_substitution(56)

# Defensive change (BOS): #18 Mitch Moreland replaces #13 Hanley Ramirez (1B), playing 1B, batting 3rd
inn.defensive_substitution(3, 18, "3")

# 8. TBR #28 Daniel Robertson (X - X - X)
inn.new_ab()
inn.pitch_list("b b b c c f b")
inn.reach("BB")
inn.advance(4, "5 2B")

# 9. TBR #8  Rob Refsnyder (X - X - 28)
inn.new_ab()
inn.pitch_list("b b c s c")
inn.out("!K")

# 1. TBR #5  Matt Duffy (X - X - 28)
inn.new_ab()
inn.pitch_list("f c b b")
inn.hit(2, rbis=1)
inn.advance(3, "27 BB")
inn.advance(4, "13 BB")

# 2. TBR #39 Kevin Kiermaier (X - 5 - X)
inn.new_ab()
inn.pitch_list("b b b 2 c s b")
inn.reach("BB")
inn.advance(2, "27 BB")
inn.advance(3, "13 BB")
inn.advance(4, "2 3B")

# 3. TBR #27 Carlos Gómez (X - 5 - 39)
inn.new_ab()
inn.pitch_list("c d t b b b")
inn.reach("BB")
inn.advance(2, "13 BB")
inn.advance(4, "2 3B")

# Pitching change (BOS): #39 Carson Smith replaces #56 Joe Kelly
inn.pitching_substitution(39)

# Offensive change (TBR): Pinch-hitter #13 Brad Miller replaces #44 C.J. Cron, batting 4th
inn.offensive_substitution(4, 13, "PH")

# 4. TBR #13 Brad Miller (5 - 39 - 27)
inn.new_ab()
inn.pitch_list("c b b d b")
inn.reach("BB", rbis=1)
inn.advance(4, "2 3B")

# 5. TBR #40 Wilson Ramos (39 - 27 - 13)
inn.new_ab()
inn.pitch_list("c c s")
inn.out("K")

# 6. TBR #2  Denard Span (39 - 27 - 13)
inn.new_ab()
inn.pitch_list("c b f d b f")
inn.hit(3, rbis=3)
inn.advance(4, "11 1B")

# 7. TBR #11 Adeiny Hechavarría (2 - X - X)
inn.new_ab()
inn.pitch_list("b b")
inn.hit(1, rbis=1)

# Offensive change (TBR): Pinch-hitter #18 Joey Wendle replaces #28 Daniel Robertson, batting 8th
inn.offensive_substitution(8, 18, "PH")

# 8. TBR #18 Joey Wendle (X - X - 11)
inn.new_ab()
inn.pitch_list("c 1 1")
inn.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TBR #37 Alex Colomé
inn = game.new_inning()

# Pitching change (TBR): #37 Alex Colomé replaces #50 Austin Pruitt
inn.pitching_substitution(37)

# Defensive switch (TBR): #13 Brad Miller moves to 1B
inn.defensive_switch(13, "3")

# Defensive change (TBR): #0 Mallex Smith replaces #2 Denard Span (LF), playing LF, batting 6th
inn.defensive_substitution(6, 0, "7")

# Defensive switch (TBR): #18 Joey Wendle moves to 2B
inn.defensive_switch(18, "4")

# 5. BOS #2  Xander Bogaerts (X - X - X)
inn.new_ab()
inn.pitch_list("c s")
inn.out("L8")

# 6. BOS #11 Rafael Devers (X - X - X)
inn.new_ab()
inn.pitch_list("b c f f b")
inn.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
inn.new_ab()
inn.pitch_list("b")
inn.hit(2)

# 8. BOS #19 Jackie Bradley Jr. (X - 36 - X)
inn.new_ab()
inn.pitch_list("c d f d")
inn.out("G4-3")

# Winning team: TBR
# WP: TBR #50 Austin Pruitt
game.winning_pitcher(50)
# SV: TBR #37 Alex Colomé
game.save_pitcher(37)

# Loser team: BOS
# LP: BOS #39 Carson Smith
game.losing_pitcher(39, is_away_team=True)

#print(game)
game.generate_scorecard()
