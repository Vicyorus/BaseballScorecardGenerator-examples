import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAA, 2018-04-18
# https://www.baseball-reference.com/boxes/ANA/ANA201804180.shtml
# https://www.mlb.com/gameday/red-sox-vs-angels/2018/04/18/529670/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-18 22:08-01:26 +1",
        "at": "Angel Stadium, Anaheim, CA",
        "att": "34,508",
        "temp": "63F, Clear",
        "wind": "8mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [13, "0"],
                [28, "7"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
                [19, "8"],
                [5, "6"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [16, "LF"],
                [7, "C"],
            ],
            "bullpen": [57, 39, 41, 61, 37, 24, 46, 76, 64, 56, 32],
        },
        "home": {
            "team": "Los Angeles Angels",
            "starter": 45,
            "roster": {
                # Lineup
                3: "Ian Kinsler",
                27: "Mike Trout",
                8: "Justin Upton",
                5: "Albert Pujols",
                56: "Kole Calhoun",
                7: "Zack Cozart",
                18: "Luis Valbuena",
                2: "Andrelton Simmons",
                12: "Martín Maldonado",
                # Starting pitcher
                45: "Tyler Skaggs",
                # Bench
                44: "René Rivera",
                17: "Shohei Ohtani",
                19: "Jefry Marte",
                24: "Chris Young",
                # Bullpen
                35: "Nick Tropeano",
                48: "Jose Alvarez",
                65: "Luke Bard",
                32: "Cam Bedrosian",
                53: "Blake Parker",
                39: "Keynan Middleton",
                46: "Blake Wood",
                28: "Andrew Heaney",
                33: "Jim Johnson",
                25: "Noé Ramirez",
                43: "Garrett Richards",
            },
            "lefties": [45, 48, 28],
            "lineup": [
                [3, "4"],
                [27, "8"],
                [8, "7"],
                [5, "0"],
                [56, "9"],
                [7, "5"],
                [18, "3"],
                [2, "6"],
                [12, "2"],
            ],
            "bench": [
                [44, "C"],
                [17, "TWP"],
                [19, "1B"],
                [24, "CF"],
            ],
            "bullpen": [35, 48, 65, 32, 53, 39, 46, 28, 33, 25, 43],
        },
        "umpires": {
            "HP": "Jordan Baker",
            "1B": "Jerry Layne",
            "2B": "Greg Gibson",
            "3B": "Vic Carapazza",
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
# Pitching: LAA #45 Tyler Skaggs
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b c c")
t1.out("G6-3")

# 2. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("b b f")
t1.hit(2)
t1.advance(4, "18 1B")

# 3. BOS #28 J.D. Martinez (X - 13 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("d b f b s s")
t1.out("K")

# 4. BOS #18 Mitch Moreland (X - 13 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b")
t1.hit(1, rbis=1)
t1.advance(2, "36 BB")
t1.advance(3, "11 PB")

# 5. BOS #36 Eduardo Núñez (X - X - 18)
t1.new_ab()
t1.pitch_list("d f f b b b")
t1.reach("BB")
t1.advance(2, "11 PB")

# 6. BOS #11 Rafael Devers (X - 18 - 36)
t1.new_ab(is_risp=True)
t1.pitch_list("b b")
t1.pb()
t1.out("(F)P5")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
b1.new_ab()
b1.pitch_list("c b f f")
b1.hit(1)
b1.advance(2, "27 1B")
b1.advance(3, "5 1B")

# 2. LAA #27 Mike Trout (X - X - 3)
b1.new_ab()
b1.pitch_list("f")
b1.hit(1)
b1.advance(2, "5 1B")

# 3. LAA #8  Justin Upton (X - 3 - 27)
b1.new_ab(is_risp=True)
b1.pitch_list("c b b s s")
b1.out("K")

# 4. LAA #5  Albert Pujols (X - 3 - 27)
b1.new_ab(is_risp=True)
b1.pitch_list("b c")
b1.hit(1)

# 5. LAA #56 Kole Calhoun (3 - 27 - 5)
b1.new_ab(is_risp=True)
b1.pitch_list("c s t")
b1.out("KT")

# 6. LAA #7  Zack Cozart (3 - 27 - 5)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b s s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAA #45 Tyler Skaggs
t2 = game.new_inning()

# 7. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("c c b c")
t2.out("!K")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("s")
t2.out("G4-3")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
t2.new_ab()
t2.pitch_list("c b s")
t2.out("G3")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 7. LAA #18 Luis Valbuena (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("L8")

# 8. LAA #2  Andrelton Simmons (X - X - X)
b2.new_ab()
b2.pitch_list("c f b")
b2.out("L6")

# 9. LAA #12 Martín Maldonado (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b b")
b2.out("L6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAA #45 Tyler Skaggs
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b b c")
t3.hit(1)
t3.advance(2, "13 FC5")
t3.advance(3, "28 1B")
t3.advance(4, "18 1B")

# 2. BOS #13 Hanley Ramirez (X - X - 50)
t3.new_ab()
t3.pitch_list("c 1 1 s 1 f f")
t3.reach("FC5")
t3.advance(2, "28 1B")
t3.advance(3, "18 1B")
t3.advance(4, "11 HR")

# 3. BOS #28 J.D. Martinez (X - 50 - 13)
t3.new_ab(is_risp=True)
t3.pitch_list("s")
t3.hit(1)
t3.advance(2, "18 1B")
t3.advance(4, "11 HR")

# 4. BOS #18 Mitch Moreland (50 - 13 - 28)
t3.new_ab(is_risp=True)
t3.pitch_list("f b")
t3.hit(1, rbis=1)
t3.advance(4, "11 HR")

# 5. BOS #36 Eduardo Núñez (13 - 28 - 18)
t3.new_ab(is_risp=True)
t3.pitch_list("f b s f d f f c")
t3.out("!K")

# 6. BOS #11 Rafael Devers (13 - 28 - 18)
t3.new_ab(is_risp=True)
t3.pitch_list("b c c")
t3.hit(4, rbis=4)

# 7. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("c b f")
t3.out("F7")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
b3.new_ab()
b3.pitch_list("c f f b")
b3.reach("HBP")
b3.advance(2, "27 1B")

# 2. LAA #27 Mike Trout (X - X - 3)
b3.new_ab()
b3.pitch_list("c b c b f")
b3.hit(1)

# 3. LAA #8  Justin Upton (X - 3 - 27)
b3.new_ab(is_risp=True)
b3.pitch_list("c")
b3.out("L8")

# 4. LAA #5  Albert Pujols (X - 3 - 27)
b3.new_ab(is_risp=True)
b3.pitch_list("c s f s")
b3.out("K")

# 5. LAA #56 Kole Calhoun (X - 3 - 27)
b3.new_ab(is_risp=True)
b3.pitch_list("f b s")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAA #45 Tyler Skaggs
t4 = game.new_inning()

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
t4.new_ab()
t4.pitch_list("c f s")
t4.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("b c b c b f")
t4.out("F7")

# 2. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.error(6)
t4.reach("E6")
t4.advance(2, "28 1B")

# 3. BOS #28 J.D. Martinez (X - X - 13)
t4.new_ab()
t4.pitch_list("s b f b b")
t4.hit(1)

# 4. BOS #18 Mitch Moreland (X - 13 - 28)
t4.new_ab(is_risp=True)
t4.pitch_list("b b 2 c s")
t4.out("G4-3")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 6. LAA #7  Zack Cozart (X - X - X)
b4.new_ab()
b4.pitch_list("c s b s")
b4.out("K")

# 7. LAA #18 Luis Valbuena (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.hit(1)
b4.thrown_out(2, "2 FC3-6", 2, 22)

# 8. LAA #2  Andrelton Simmons (X - X - 18)
b4.new_ab()
b4.reach("FC3-6")

# 9. LAA #12 Martín Maldonado (X - X - 2)
b4.new_ab()
b4.pitch_list("c b f b c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAA #45 Tyler Skaggs
t5 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("f b b c b")
t5.hit(1)
t5.thrown_out(2, "7-4", 1, 45)

# Pitching change (LAA): #48 Jose Alvarez replaces #45 Tyler Skaggs
t5.pitching_substitution(48)

# 6. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("c b c b c")
t5.out("!K")

# 7. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("f b s")
t5.out("G3")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("f b f")
b5.hit(1)

# 2. LAA #27 Mike Trout (X - X - 3)
b5.new_ab()
b5.pitch_list("b b c b c")
b5.out("F8")

# 3. LAA #8  Justin Upton (X - X - 3)
b5.new_ab()
b5.pitch_list("c s b")
b5.out("L9")

# 4. LAA #5  Albert Pujols (X - X - 3)
b5.new_ab()
b5.pitch_list("c b s b")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAA #48 Jose Alvarez
t6 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.out("L7")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f b f s")
t6.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)

# Pitching change (LAA): #46 Blake Wood replaces #48 Jose Alvarez
t6.pitching_substitution(46)

# 2. BOS #13 Hanley Ramirez (X - X - 50)
t6.new_ab()
t6.pitch_list("b f s c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 5. LAA #56 Kole Calhoun (X - X - X)
b6.new_ab()
b6.pitch_list("c c b f f b")
b6.out("G4-3")

# 6. LAA #7  Zack Cozart (X - X - X)
b6.new_ab()
b6.pitch_list("c f f")
b6.out("G6-3")

# 7. LAA #18 Luis Valbuena (X - X - X)
b6.new_ab()
b6.out("L9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAA #46 Blake Wood
t7 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(4)

# 4. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")
t7.thrown_out(2, "36 DP3-6-3", 1, 46)

# 5. BOS #36 Eduardo Núñez (X - X - 18)
t7.new_ab()
t7.pitch_list("b b c")
t7.out("DP3-6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("f s s")
t7.out("K")


# Bot 7th
# Pitching: BOS #39 Carson Smith
b7 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #22 Rick Porcello
b7.pitching_substitution(39)

# 8. LAA #2  Andrelton Simmons (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F9")

# 9. LAA #12 Martín Maldonado (X - X - X)
b7.new_ab()
b7.pitch_list("c b c s")
b7.out("K")

# 1. LAA #3  Ian Kinsler (X - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")

# 2. LAA #27 Mike Trout (X - X - 3)
b7.new_ab()
b7.pitch_list("c")
b7.out("(F)P3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAA #32 Cam Bedrosian
t8 = game.new_inning()

# Pitching change (LAA): #32 Cam Bedrosian replaces #46 Blake Wood
t8.pitching_substitution(32)

# 7. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.pitch_list("c s s")
t8.out("K")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("b f f")
t8.hit(2)
t8.advance(3, "50 FC7-4")

# 9. BOS #5  Tzu-Wei Lin (X - 19 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b c c d f d b")
t8.reach("BB")
t8.thrown_out(2, "50 FC7-4", 2, 32)

# 1. BOS #50 Mookie Betts (X - 19 - 5)
t8.new_ab(is_risp=True)
t8.pitch_list("c f f")
t8.reach("FC7-4")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #13 Hanley Ramirez, batting 2nd
t8.offensive_substitution(2, 23, "PH")

# 2. BOS #23 Blake Swihart (19 - X - 50)
t8.new_ab(is_risp=True)
t8.pitch_list("c s s")
t8.out("K")


# Bot 8th
# Pitching: BOS #64 Marcus Walden
b8 = game.new_inning()

# Pitching change (BOS): #64 Marcus Walden replaces #39 Carson Smith
b8.pitching_substitution(64)

# Defensive switch (BOS): #23 Blake Swihart moves to DH
b8.defensive_switch(23, "0")

# 3. LAA #8  Justin Upton (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b f f c")
b8.out("!K")

# 4. LAA #5  Albert Pujols (X - X - X)
b8.new_ab()
b8.pitch_list("s f")
b8.out("P4")

# 5. LAA #56 Kole Calhoun (X - X - X)
b8.new_ab()
b8.pitch_list("b f c")
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAA #39 Keynan Middleton
t9 = game.new_inning()

# Pitching change (LAA): #39 Keynan Middleton replaces #32 Cam Bedrosian
t9.pitching_substitution(39)

# 3. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("c b c f b f b f")
t9.hit(1)
t9.advance(4, "18 HR")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t9.new_ab()
t9.hit(4, rbis=2)

# 5. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c f f s")
t9.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b b s f b")
t9.hit(2)

# 7. BOS #3  Sandy León (X - 11 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("f c d f b b t")
t9.out("KT")

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b")
t9.out("L9")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #64 Marcus Walden
b9.pitching_substitution(46)

# 6. LAA #7  Zack Cozart (X - X - X)
b9.new_ab()
b9.out("G5-3")

# 7. LAA #18 Luis Valbuena (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.out("F8")

# 8. LAA #2  Andrelton Simmons (X - X - X)
b9.new_ab()
b9.pitch_list("b f c b")
b9.out("G6-3")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)

# Loser team: LAA
# LP: LAA #45 Tyler Skaggs
game.losing_pitcher(45)

# print(game)
game.generate_scorecard()
