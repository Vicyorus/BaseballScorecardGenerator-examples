import os
from baseball_scorecard.baseball_scorecard import Scorecard

# LAA @ BOS, 2018-06-27
# https://www.baseball-reference.com/boxes/BOS/BOS201806270.shtml
# https://www.mlb.com/gameday/angels-vs-red-sox/2018/06/27/530605/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-27 19:12-23:12",
        "at": "Fenway Park, Boston, MA",
        "att": "37,521",
        "temp": "73F, Partly Cloudy",
        "wind": "13mph, Out To LF",
        "away": {
            "team": "Los Angeles Angels",
            "starter": 28,
            "roster": {
                # Lineup
                3: "Ian Kinsler",
                27: "Mike Trout",
                8: "Justin Upton",
                5: "Albert Pujols",
                18: "Luis Valbuena",
                2: "Andrelton Simmons",
                56: "Kole Calhoun",
                12: "Martín Maldonado",
                59: "Michael Hermosillo",
                # Starting pitcher
                28: "Andrew Heaney",
                # Bench
                6: "David Fletcher",
                10: "José Briceño",
                16: "Nolan Fontana",
                24: "Chris Young",
                # Bullpen
                68: "Deck McGuire",
                45: "Tyler Skaggs",
                48: "Jose Alvarez",
                64: "Félix Peña",
                32: "Cam Bedrosian",
                51: "Jaime Barria",
                53: "Blake Parker",
                57: "Hansel Robles",
                38: "Justin Anderson",
                25: "Noé Ramirez",
                65: "Jake Jewell",
            },
            "lefties": [28, 45, 48],
            "lineup": [
                [3, "4"],
                [27, "0"],
                [8, "7"],
                [5, "3"],
                [18, "5"],
                [2, "6"],
                [56, "9"],
                [12, "2"],
                [59, "8"],
            ],
            "bench": [
                [6, "2B"],
                [10, "C"],
                [16, "2B"],
                [24, "CF"],
            ],
            "bullpen": [68, 45, 48, 64, 32, 51, 53, 57, 38, 25, 65],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                5: "Tzu-Wei Lin",
                12: "Brock Holt",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [12, "2B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 44, 41, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "umpires": {
            "HP": "Gabe Morales",
            "1B": "Ed Hickox",
            "2B": "Jerry Meals",
            "3B": "Chris Segal",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
t1.new_ab()
t1.pitch_list("b c b s s")
t1.out("K")

# 2. LAA #27 Mike Trout (X - X - X)
t1.new_ab()
t1.out("G5-3")

# 3. LAA #8  Justin Upton (X - X - X)
t1.new_ab()
t1.pitch_list("b b c b f")
t1.out("G6-3")


# Bot 1st
# Pitching: LAA #28 Andrew Heaney
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.hit(1)
b1.thrown_out(2, "16 FC1-6", 1, 28)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("f f")
b1.reach("FC1-6")
b1.advance(2, "28 SB")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b1.new_ab()
b1.pitch_list("c b c b b f b")
b1.reach("BB")

# 4. BOS #2  Xander Bogaerts (X - 16 - 28)
b1.new_ab()
b1.pitch_list("c f d s")
b1.out("K")

# 5. BOS #18 Mitch Moreland (X - 16 - 28)
b1.new_ab()
b1.pitch_list("s f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 4. LAA #5  Albert Pujols (X - X - X)
t2.new_ab()
t2.pitch_list("b c f")
t2.out("P3")

# 5. LAA #18 Luis Valbuena (X - X - X)
t2.new_ab()
t2.pitch_list("c c b c")
t2.out("!K")

# 6. LAA #2  Andrelton Simmons (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b b")
t2.hit(1)
t2.advance(3, "56 1B")

# 7. LAA #56 Kole Calhoun (X - X - 2)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)

# 8. LAA #12 Martín Maldonado (2 - X - 56)
t2.new_ab()
t2.pitch_list("b b c c f")
t2.out("F9")


# Bot 2nd
# Pitching: LAA #28 Andrew Heaney
b2 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(4, rbis=1)

# 7. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("s")
b2.hit(1)
b2.advance(4, "3 HR")

# 8. BOS #3  Sandy León (X - X - 11)
b2.new_ab()
b2.pitch_list("c b 1 b b")
b2.hit(4, rbis=2)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c b f s")
b2.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("b b c c b b")
b2.reach("BB")
b2.advance(3, "16 1B")
b2.advance(4, "28 HR")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b2.new_ab()
b2.pitch_list("1 f")
b2.hit(1)
b2.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (50 - X - 16)
b2.new_ab()
b2.hit(4, rbis=3)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.out("F8")

# 5. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c f f")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 9. LAA #59 Michael Hermosillo (X - X - X)
t3.new_ab()
t3.pitch_list("f c b t")
t3.out("KT")

# 1. LAA #3  Ian Kinsler (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G5-3")

# 2. LAA #27 Mike Trout (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(1)
t3.advance(2, "8 BB")

# 3. LAA #8  Justin Upton (X - X - 27)
t3.new_ab()
t3.pitch_list("c c f b b b b")
t3.reach("BB")

# 4. LAA #5  Albert Pujols (X - 27 - 8)
t3.new_ab()
t3.pitch_list("c s b")
t3.out("F9")


# Bot 3rd
# Pitching: LAA #28 Andrew Heaney
b3 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("L8")

# 7. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("f b")
b3.out("L5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 5. LAA #18 Luis Valbuena (X - X - X)
t4.new_ab()
t4.pitch_list("s b b")
t4.hit(2)

# 6. LAA #2  Andrelton Simmons (X - 18 - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("G5-3")

# 7. LAA #56 Kole Calhoun (X - 18 - X)
t4.new_ab()
t4.pitch_list("c c s")
t4.out("K")

# 8. LAA #12 Martín Maldonado (X - 18 - X)
t4.new_ab()
t4.pitch_list("f f b b d f b")
t4.reach("BB")

# 9. LAA #59 Michael Hermosillo (X - 18 - 12)
t4.new_ab()
t4.pitch_list("f d")
t4.out("P3")


# Bot 4th
# Pitching: LAA #28 Andrew Heaney
b4 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("f b s b")
b4.hit(1)
b4.advance(2, "50 BB")
b4.advance(3, "28 1B")
b4.thrown_out(4, "2 FC5-2", 2, 57)

# 1. BOS #50 Mookie Betts (X - X - 19)
b4.new_ab()
b4.pitch_list("b b b c b")
b4.reach("BB")
b4.advance(2, "28 1B")
b4.advance(3, "2 FC5-2")

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
b4.new_ab()
b4.pitch_list("c t d")
b4.out("F8")

# 3. BOS #28 J.D. Martinez (X - 19 - 50)
b4.new_ab()
b4.pitch_list("b f b b")
b4.hit(1)
b4.advance(2, "2 FC5-2")

# Pitching change (LAA): #57 Hansel Robles replaces #28 Andrew Heaney
b4.pitching_substitution(57)

# 4. BOS #2  Xander Bogaerts (19 - 50 - 28)
b4.new_ab()
b4.pitch_list("c d f")
b4.reach("FC5-2")
b4.thrown_out(2, "18 FC3-6", 3, 57)

# 5. BOS #18 Mitch Moreland (50 - 28 - 2)
b4.new_ab()
b4.pitch_list("b f t f d")
b4.reach("FC3-6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
t5.new_ab()
t5.hit(4, rbis=1)

# 2. LAA #27 Mike Trout (X - X - X)
t5.new_ab()
t5.pitch_list("c b c t")
t5.out("KT")

# 3. LAA #8  Justin Upton (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G6-3")

# 4. LAA #5  Albert Pujols (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("F8")


# Bot 5th
# Pitching: LAA #32 Cam Bedrosian
b5 = game.new_inning()

# Pitching change (LAA): #32 Cam Bedrosian replaces #57 Hansel Robles
b5.pitching_substitution(32)

# 6. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c b s b b")
b5.out("G5-3")

# 7. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("c s b b f f b")
b5.hit(1)
b5.advance(2, "3 SB")

# 8. BOS #3  Sandy León (X - X - 11)
b5.new_ab()
b5.pitch_list("s d c s")
b5.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 5. LAA #18 Luis Valbuena (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F7")

# 6. LAA #2  Andrelton Simmons (X - X - X)
t6.new_ab()
t6.pitch_list("c b c f b f b f")
t6.hit(1)
t6.advance(3, "56 1B")
t6.advance(4, "12 HR")

# 7. LAA #56 Kole Calhoun (X - X - 2)
t6.new_ab()
t6.hit(1)
t6.advance(4, "12 HR")

# 8. LAA #12 Martín Maldonado (2 - X - 56)
t6.new_ab()
t6.pitch_list("d s f")
t6.hit(4, rbis=3)

# 9. LAA #59 Michael Hermosillo (X - X - X)
t6.new_ab()
t6.pitch_list("s")
t6.out("G6-3")

# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello
t6.pitching_substitution(37)

# 1. LAA #3  Ian Kinsler (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("F9")


# Bot 6th
# Pitching: LAA #38 Justin Anderson
b6 = game.new_inning()

# Pitching change (LAA): #38 Justin Anderson replaces #32 Cam Bedrosian
b6.pitching_substitution(38)

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b c f")
b6.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
t7.pitching_substitution(56)

# 2. LAA #27 Mike Trout (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("P3")

# 3. LAA #8  Justin Upton (X - X - X)
t7.new_ab()
t7.pitch_list("b f b c f f")
t7.hit(1)
t7.advance(3, "5 1B")
t7.advance(4, "18 E1")

# 4. LAA #5  Albert Pujols (X - X - 8)
t7.new_ab()
t7.hit(1)
t7.advance(2, "18 E1")
t7.advance("U", "2 2B")

# 5. LAA #18 Luis Valbuena (8 - X - 5)
t7.new_ab()
t7.pitch_list("b c b")
t7.error(1)
t7.reach("E1", rbis=1)
t7.advance(3, "2 2B")

# 6. LAA #2  Andrelton Simmons (X - 5 - 18)
t7.new_ab()
t7.pitch_list("b")
t7.hit(2, rbis=1)

# 7. LAA #56 Kole Calhoun (18 - 2 - X)
t7.new_ab()
t7.pitch_list("s s b b f c")
t7.out("!K")

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t7.pitching_substitution(32)

# 8. LAA #12 Martín Maldonado (18 - 2 - X)
t7.new_ab()
t7.pitch_list("c b s f s")
t7.out("K2-3")


# Bot 7th
# Pitching: LAA #48 Jose Alvarez
b7 = game.new_inning()

# Pitching change (LAA): #48 Jose Alvarez replaces #38 Justin Anderson
b7.pitching_substitution(48)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c s f f")
b7.out("F9")

# 5. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("b b c")
b7.out("G4-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(4, "11 E6")

# 7. BOS #11 Rafael Devers (X - X - 36)
b7.new_ab()
b7.pitch_list("f b 1")
b7.hit(2, rbis=1)
b7.error(6)
b7.advance(3, "E6")
b7.advance(4, "3 1B")

# 8. BOS #3  Sandy León (11 - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
b7.new_ab()
b7.pitch_list("c b s b f f d")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Offensive change (LAA): Pinch-hitter #6 David Fletcher replaces #59 Michael Hermosillo, batting 9th
t8.offensive_substitution(9, 6, "PH")

# 9. LAA #6  David Fletcher (X - X - X)
t8.new_ab()
t8.pitch_list("b c c b s")
t8.out("K")

# 1. LAA #3  Ian Kinsler (X - X - X)
t8.new_ab()
t8.error(5)
t8.reach("E5")
t8.advance(2, "27 BB")
t8.advance(3, "5 WP")

# 2. LAA #27 Mike Trout (X - X - 3)
t8.new_ab()
t8.pitch_list("c f 1 b d 1 b b")
t8.reach("BB")
t8.advance(2, "5 WP")

# 3. LAA #8  Justin Upton (X - 3 - 27)
t8.new_ab()
t8.pitch_list("c c d b s")
t8.out("K")

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t8.pitching_substitution(46)

# 4. LAA #5  Albert Pujols (X - 3 - 27)
t8.new_ab()
t8.pitch_list("c b c f b b b")
t8.wp()
t8.reach("BB")
# Offensive change (LAA): Pinch-runner #24 Chris Young replaces #5 Albert Pujols
t8.offensive_substitution(4, 24, "PR")
t8.atbase("PR")

# 5. LAA #18 Luis Valbuena (3 - 27 - 5)
t8.new_ab()
t8.pitch_list("s b b d c s")
t8.out("K")


# Bot 8th
# Pitching: LAA #65 Jake Jewell
b8 = game.new_inning()

# Pitching change (LAA): #65 Jake Jewell replaces #48 Jose Alvarez
b8.pitching_substitution(65)

# Defensive switch (LAA): #24 Chris Young moves to CF
b8.defensive_switch(24, "8")

# Defensive switch (LAA): #18 Luis Valbuena moves to 1B
b8.defensive_switch(18, "3")

# Defensive switch (LAA): #6 David Fletcher moves to 3B
b8.defensive_switch(6, "5")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("c b b")
b8.out("F7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("b s b b b")
b8.reach("BB")
b8.thrown_out(2, "28 FC5-4", 2, 65)

# 3. BOS #28 J.D. Martinez (X - X - 16)
b8.new_ab()
b8.pitch_list("1 b 1 b 1 1 s f 1")
b8.reach("FC5-4")
b8.advance(3, "2 2B")
b8.advance(4, "18 WP")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
b8.new_ab()
b8.pitch_list("b f b b c f")
b8.hit(2)
b8.advance(3, "18 WP")

# Pitching change (LAA): #53 Blake Parker replaces #65 Jake Jewell
b8.pitching_substitution(53)

# 5. BOS #18 Mitch Moreland (28 - 2 - X)
b8.new_ab()
b8.pitch_list("b c 2 f b d")
b8.wp()
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# 6. LAA #2  Andrelton Simmons (X - X - X)
t9.new_ab()
t9.pitch_list("c b b c")
t9.out("P3")

# 7. LAA #56 Kole Calhoun (X - X - X)
t9.new_ab()
t9.pitch_list("b b f c")
t9.out("G5-3")

# 8. LAA #12 Martín Maldonado (X - X - X)
t9.new_ab()
t9.pitch_list("c b b t s")
t9.out("K2-3")

# Winning team: BOS
# WP: BOS #32 Matt Barnes
game.winning_pitcher(32)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: LAA
# LP: LAA #48 Jose Alvarez
game.losing_pitcher(48, is_away_team=True)

# print(game)
game.generate_scorecard()
