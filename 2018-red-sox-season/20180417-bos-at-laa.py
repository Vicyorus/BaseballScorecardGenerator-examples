import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ LAA, 2018-04-17
# https://www.baseball-reference.com/boxes/ANA/ANA201804170.shtml
# https://www.mlb.com/gameday/red-sox-vs-angels/2018/04/17/529655/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-17 22:09-01:24 +1",
        "at": "Angel Stadium, Anaheim, CA",
        "att": "44,822",
        "temp": "67F, Clear",
        "wind": "8mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                12: "Brock Holt",
                # Starting pitcher
                24: "David Price",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
                [12, "6"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 39, 22, 41, 61, 37, 46, 76, 64, 56, 32],
        },
        "home": {
            "team": "Los Angeles Angels",
            "starter": 17,
            "roster": {
                # Lineup
                3: "Ian Kinsler",
                27: "Mike Trout",
                8: "Justin Upton",
                5: "Albert Pujols",
                7: "Zack Cozart",
                56: "Kole Calhoun",
                2: "Andrelton Simmons",
                19: "Jefry Marte",
                12: "Martín Maldonado",
                # Starting pitcher
                17: "Shohei Ohtani",
                # Bench
                44: "René Rivera",
                18: "Luis Valbuena",
                24: "Chris Young",
                # Bullpen
                35: "Nick Tropeano",
                45: "Tyler Skaggs",
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
                [7, "5"],
                [56, "9"],
                [2, "6"],
                [19, "3"],
                [12, "2"],
            ],
            "bench": [
                [44, "C"],
                [18, "3B"],
                [24, "CF"],
            ],
            "bullpen": [35, 45, 48, 65, 32, 53, 39, 46, 28, 33, 25, 43],
        },
        "umpires": {
            "HP": "Vic Carapazza",
            "1B": "Jordan Baker",
            "2B": "Jerry Layne",
            "3B": "Greg Gibson",
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
# Pitching: LAA #17 Shohei Ohtani
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b f f b b f")
t1.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b f b b t")
t1.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b")
t1.hit(1)
t1.advance(2, "11 WP")

# 4. BOS #28 J.D. Martinez (X - X - 13)
t1.new_ab()
t1.pitch_list("b c b f b s")
t1.out("K")

# 5. BOS #11 Rafael Devers (X - X - 13)
t1.new_ab(is_risp=True)
t1.pitch_list("b s b")
t1.wp()
t1.out("(F)P5")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. LAA #3  Ian Kinsler (X - X - X)
b1.new_ab()
b1.pitch_list("b s")
b1.out("G1-3")

# 2. LAA #27 Mike Trout (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.thrown_out(2, "5 FC5-4", 3, 24)

# 3. LAA #8  Justin Upton (X - X - 27)
b1.new_ab()
b1.pitch_list("b s c b s")
b1.out("K")

# 4. LAA #5  Albert Pujols (X - X - 27)
b1.new_ab()
b1.pitch_list("c")
b1.reach("FC5-4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: LAA #17 Shohei Ohtani
t2 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("L8")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("f b")
t2.hit(1)
t2.advance(2, "7 BB")
t2.advance(4, "12 1B")

# 8. BOS #7  Christian Vázquez (X - X - 19)
t2.new_ab()
t2.pitch_list("b f f b 1 b 1 f b")
t2.reach("BB")
t2.advance(2, "12 1B")
t2.advance(3, "50 BB")
t2.advance(4, "16 SF7")

# 9. BOS #12 Brock Holt (X - 19 - 7)
t2.new_ab(is_risp=True)
t2.pitch_list("c b b")
t2.hit(1, rbis=1)
t2.advance(2, "50 BB")

# 1. BOS #50 Mookie Betts (X - 7 - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("c c f b b f b f b")
t2.reach("BB")

# 2. BOS #16 Andrew Benintendi (7 - 12 - 50)
t2.new_ab(is_risp=True)
t2.pitch_list("b f b b")
t2.out("SF7", rbis=1)

# 3. BOS #13 Hanley Ramirez (X - 12 - 50)
t2.new_ab(is_risp=True)
t2.pitch_list("d c b f f b")
t2.out("G6-3")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 5. LAA #7  Zack Cozart (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G6-3")

# 6. LAA #56 Kole Calhoun (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G4-3")

# 7. LAA #2  Andrelton Simmons (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b s b")
b2.reach("BB")

# 8. LAA #19 Jefry Marte (X - X - 2)
b2.new_ab()
b2.pitch_list("b c b c")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: LAA #65 Luke Bard
t3 = game.new_inning()

# Pitching change (LAA): #65 Luke Bard replaces #17 Shohei Ohtani
t3.pitching_substitution(65)

# 4. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.thrown_out(2, "36 FC1-4-6", 2, 65)

# 5. BOS #11 Rafael Devers (X - X - 28)
t3.new_ab()
t3.pitch_list("s b f f s")
t3.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - 28)
t3.new_ab()
t3.reach("FC1-4-6")
t3.advance(4, "19 HR")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 36)
t3.new_ab()
t3.pitch_list("c d b")
t3.hit(4, rbis=2)

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.reach("HBP")
t3.advance(4, "12 HR")

# 9. BOS #12 Brock Holt (X - X - 7)
t3.new_ab()
t3.pitch_list("c b f d b")
t3.hit(4, rbis=2)

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("G1-3")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 9. LAA #12 Martín Maldonado (X - X - X)
b3.new_ab()
b3.pitch_list("b c b b f b")
b3.reach("BB")
b3.advance(3, "8 1B")
b3.advance(4, "5 1B")

# 1. LAA #3  Ian Kinsler (X - X - 12)
b3.new_ab()
b3.out("P6")

# 2. LAA #27 Mike Trout (X - X - 12)
b3.new_ab()
b3.pitch_list("c f b b f t")
b3.out("KT")

# 3. LAA #8  Justin Upton (X - X - 12)
b3.new_ab()
b3.hit(1)
b3.advance(2, "5 1B")

# 4. LAA #5  Albert Pujols (12 - X - 8)
b3.new_ab(is_risp=True)
b3.pitch_list("b")
b3.hit(1, rbis=1)

# 5. LAA #7  Zack Cozart (X - 8 - 5)
b3.new_ab(is_risp=True)
b3.pitch_list("b c c c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: LAA #65 Luke Bard
t4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("c f f b")
t4.out("L7")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("s")
t4.out("F9")

# 5. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.hit(4)

# 6. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("f b")
t4.hit(1)
t4.advance(2, "19 1B")
t4.advance(3, "7 1B")
t4.thrown_out(4, "7 9-2", 3, 53)

# Pitching change (LAA): #53 Blake Parker replaces #65 Luke Bard
t4.pitching_substitution(53)

# 7. BOS #19 Jackie Bradley Jr. (X - X - 36)
t4.new_ab()
t4.pitch_list("s")
t4.hit(1)
t4.advance(2, "7 9-2")

# 8. BOS #7  Christian Vázquez (X - 36 - 19)
t4.new_ab(is_risp=True)
t4.pitch_list("b")
t4.hit(1)


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 6. LAA #56 Kole Calhoun (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.out("G4-3")

# 7. LAA #2  Andrelton Simmons (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b c b")
b4.reach("BB")

# 8. LAA #19 Jefry Marte (X - X - 2)
b4.new_ab()
b4.pitch_list("f")
b4.out("P6")

# 9. LAA #12 Martín Maldonado (X - X - 2)
b4.new_ab()
b4.pitch_list("f s f b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: LAA #53 Blake Parker
t5 = game.new_inning()

# 9. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("b f s f")
t5.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c b t b f b b")
t5.reach("BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.out("F8")

# 3. BOS #13 Hanley Ramirez (X - X - 50)
t5.new_ab()
t5.pitch_list("b s b c d")
t5.out("L4")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# Defensive change (BOS): #5 Tzu-Wei Lin replaces #16 Andrew Benintendi (LF), playing SS, batting 2nd
b5.defensive_substitution(2, 5, "6")

# Defensive switch (BOS): #12 Brock Holt moves to LF
b5.defensive_switch(12, "7")

# 1. LAA #3  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("F7")

# 2. LAA #27 Mike Trout (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)

# 3. LAA #8  Justin Upton (X - X - 27)
b5.new_ab()
b5.pitch_list("b c t s")
b5.out("K")

# 4. LAA #5  Albert Pujols (X - X - 27)
b5.new_ab()
b5.pitch_list("c b f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: LAA #25 Noé Ramirez
t6 = game.new_inning()

# Pitching change (LAA): #25 Noé Ramirez replaces #53 Blake Parker
t6.pitching_substitution(25)

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #28 J.D. Martinez, batting 4th
t6.offensive_substitution(4, 23, "PH")

# 4. BOS #23 Blake Swihart (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b c")
t6.out("G1-3")

# 5. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.hit(1)
t6.thrown_out(1, "36 DP3", 3, 25)

# 6. BOS #36 Eduardo Núñez (X - X - 11)
t6.new_ab()
t6.pitch_list("b")
t6.out("DP3")


# Bot 6th
# Pitching: BOS #61 Brian Johnson
b6 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #24 David Price
b6.pitching_substitution(61)

# Defensive switch (BOS): #23 Blake Swihart moves to DH
b6.defensive_switch(23, "0")

# 5. LAA #7  Zack Cozart (X - X - X)
b6.new_ab()
b6.pitch_list("b c f b s")
b6.out("K")

# 6. LAA #56 Kole Calhoun (X - X - X)
b6.new_ab()
b6.out("F8")

# 7. LAA #2  Andrelton Simmons (X - X - X)
b6.new_ab()
b6.pitch_list("c s c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: LAA #25 Noé Ramirez
t7 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b s f b f")
t7.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("P6")

# 9. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("b f f")
t7.out("F7")


# Bot 7th
# Pitching: BOS #61 Brian Johnson
b7 = game.new_inning()

# 8. LAA #19 Jefry Marte (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.hit(1)
b7.error(5)
b7.advance(2, "12 E5")
b7.advance(3, "3 DP5-4-3")

# 9. LAA #12 Martín Maldonado (X - X - 19)
b7.new_ab()
b7.pitch_list("c f f b f")
b7.reach("FC5")
b7.thrown_out(2, "3 DP5-4-3", 1, 61)

# 1. LAA #3  Ian Kinsler (X - 19 - 12)
b7.new_ab(is_risp=True)
b7.pitch_list("b f b c f")
b7.out("DP5-4-3")

# 2. LAA #27 Mike Trout (19 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b b f b b")
b7.reach("BB")

# 3. LAA #8  Justin Upton (19 - X - 27)
b7.new_ab(is_risp=True)
b7.pitch_list("s c b")
b7.out("L7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: LAA #32 Cam Bedrosian
t8 = game.new_inning()

# Pitching change (LAA): #32 Cam Bedrosian replaces #25 Noé Ramirez
t8.pitching_substitution(32)

# Defensive change (LAA): #24 Chris Young replaces #27 Mike Trout (CF), playing CF, batting 2nd
t8.defensive_substitution(2, 24, "8")

# Defensive switch (LAA): #7 Zack Cozart moves to SS
t8.defensive_switch(7, "6")

# Defensive change (LAA): #18 Luis Valbuena replaces #2 Andrelton Simmons (SS), playing 3B, batting 7th
t8.defensive_substitution(7, 18, "5")

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.hit(4)

# 2. BOS #5  Tzu-Wei Lin (X - X - X)
t8.new_ab()
t8.pitch_list("c s b c")
t8.out("!K")

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #13 Hanley Ramirez, batting 3rd
t8.offensive_substitution(3, 18, "PH")

# 3. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("f b b b b")
t8.reach("BB")
t8.thrown_out(2, "23 FC3-6", 2, 32)

# 4. BOS #23 Blake Swihart (X - X - 18)
t8.new_ab()
t8.pitch_list("c b")
t8.reach("FC3-6")

# 5. BOS #11 Rafael Devers (X - X - 23)
t8.new_ab()
t8.out("G3-1")


# Bot 8th
# Pitching: BOS #61 Brian Johnson
b8 = game.new_inning()

# Defensive switch (BOS): #18 Mitch Moreland moves to 1B
b8.defensive_switch(18, "3")

# Offensive change (LAA): Pinch-hitter #44 René Rivera replaces #5 Albert Pujols, batting 4th
b8.offensive_substitution(4, 44, "PH")

# 4. LAA #44 René Rivera (X - X - X)
b8.new_ab()
b8.pitch_list("f f s")
b8.out("K")

# 5. LAA #7  Zack Cozart (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b b")
b8.reach("BB")
b8.thrown_out(2, "56 DP6-3", 2, 61)

# 6. LAA #56 Kole Calhoun (X - X - 7)
b8.new_ab()
b8.out("DP6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: LAA #33 Jim Johnson
t9 = game.new_inning()

# Pitching change (LAA): #33 Jim Johnson replaces #32 Cam Bedrosian
t9.pitching_substitution(33)

# Defensive switch (LAA): #44 René Rivera moves to DH
t9.defensive_switch(44, "0")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
t9.advance(2, "7 1B")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 36)
t9.new_ab()
t9.pitch_list("c b d f b f")
t9.out("L9")

# 8. BOS #7  Christian Vázquez (X - X - 36)
t9.new_ab()
t9.pitch_list("b b c")
t9.hit(1)
t9.thrown_out(2, "12 DP4-6-3", 2, 33)

# 9. BOS #12 Brock Holt (X - 36 - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("b b")
t9.out("DP4-6-3")


# Bot 9th
# Pitching: BOS #64 Marcus Walden
b9 = game.new_inning()

# Pitching change (BOS): #64 Marcus Walden replaces #61 Brian Johnson
b9.pitching_substitution(64)

# 7. LAA #18 Luis Valbuena (X - X - X)
b9.new_ab()
b9.pitch_list("f f b b s")
b9.out("K")

# 8. LAA #19 Jefry Marte (X - X - X)
b9.new_ab()
b9.out("G5-3")

# 9. LAA #12 Martín Maldonado (X - X - X)
b9.new_ab()
b9.pitch_list("b c")
b9.out("G6-3")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24, is_away_team=True)

# Loser team: LAA
# LP: LAA #17 Shohei Ohtani
game.losing_pitcher(17)

# print(game)
game.generate_scorecard()
