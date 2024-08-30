import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ MIN, 2018-06-19
# https://www.baseball-reference.com/boxes/MIN/MIN201806190.shtml
# https://www.mlb.com/gameday/red-sox-vs-twins/2018/06/19/530492/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-19 20:11-23:25",
        "at": "Target Field, Minneapolis, MN",
        "att": "28,550",
        "temp": "69F, Overcast",
        "wind": "8mph, In From LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                61: "Brian Johnson",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 61, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [2, "6"],
                [28, "0"],
                [18, "3"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 44, 22, 61, 37, 63, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Minnesota Twins",
            "starter": 17,
            "roster": {
                # Lineup
                7: "Joe Mauer",
                20: "Eddie Rosario",
                5: "Eduardo Escobar",
                2: "Brian Dozier",
                36: "Robbie Grossman",
                16: "Ehire Adrianza",
                45: "Taylor Motter",
                23: "Mitch Garver",
                24: "Ryan LaMarre",
                # Starting pitcher
                17: "José Berríos",
                # Bench
                46: "Bobby Wilson",
                99: "Logan Morrison",
                26: "Max Kepler",
                # Bullpen
                77: "Fernando Romero",
                38: "Matt Belisle",
                43: "Addison Reed",
                31: "Lance Lynn",
                68: "Matt Magill",
                39: "Trevor Hildenberger",
                12: "Jake Odorizzi",
                56: "Fernando Rodney",
                57: "Ryan Pressly",
                55: "Taylor Rogers",
                32: "Zach Duke",
                44: "Kyle Gibson",
            },
            "lefties": [55, 32],
            "lineup": [
                [7, "3"],
                [20, "7"],
                [5, "5"],
                [2, "4"],
                [36, "0"],
                [16, "6"],
                [45, "9"],
                [23, "2"],
                [24, "8"],
            ],
            "bench": [
                [46, "C"],
                [99, "1B"],
                [26, "RF"],
            ],
            "bullpen": [77, 38, 43, 31, 68, 39, 12, 56, 57, 55, 32, 44],
        },
        "umpires": {
            "HP": "Carlos Torres",
            "1B": "Jeff Nelson",
            "2B": "Tom Woodring",
            "3B": "Scott Barry",
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
# Pitching: MIN #17 José Berríos
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c b")
t1.reach("BB")
t1.advance(2, "16 G1-3")
t1.advance(3, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("s 1 1 1 1 b")
t1.out("G1-3")

# 3. BOS #2  Xander Bogaerts (X - 50 - X)
t1.new_ab()
t1.pitch_list("b c d f t")
t1.out("KT")

# 4. BOS #28 J.D. Martinez (X - 50 - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)

# 5. BOS #18 Mitch Moreland (50 - X - 28)
t1.new_ab()
t1.pitch_list("b f c s")
t1.out("K")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
b1.new_ab()
b1.pitch_list("c b b s b f f f s")
b1.out("K")

# 2. MIN #20 Eddie Rosario (X - X - X)
b1.new_ab()
b1.out("F8")

# 3. MIN #5  Eduardo Escobar (X - X - X)
b1.new_ab()
b1.pitch_list("c f b b c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: MIN #17 José Berríos
t2 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("s b b")
t2.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b c f")
t2.out("P5")

# 8. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.out("B1-3")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 4. MIN #2  Brian Dozier (X - X - X)
b2.new_ab()
b2.out("G5-3")

# 5. MIN #36 Robbie Grossman (X - X - X)
b2.new_ab()
b2.pitch_list("c c f s")
b2.out("K")

# 6. MIN #16 Ehire Adrianza (X - X - X)
b2.new_ab()
b2.pitch_list("f f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: MIN #17 José Berríos
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b b")
t3.reach("BB")
t3.advance(2, "50 WP")
t3.error(1)
t3.advance(3, "16 POE1")

# 1. BOS #50 Mookie Betts (X - X - 19)
t3.new_ab()
t3.pitch_list("c b b b f")
t3.wp()
t3.out("L7")

# 2. BOS #16 Andrew Benintendi (X - 19 - X)
t3.new_ab()
t3.pitch_list("b 2 s b f b f s")
t3.out("K")

# 3. BOS #2  Xander Bogaerts (19 - X - X)
t3.new_ab()
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 7. MIN #45 Taylor Motter (X - X - X)
b3.new_ab()
b3.out("G3")

# 8. MIN #23 Mitch Garver (X - X - X)
b3.new_ab()
b3.pitch_list("c b c c")
b3.out("!K")

# 9. MIN #24 Ryan LaMarre (X - X - X)
b3.new_ab()
b3.pitch_list("c b b")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: MIN #17 José Berríos
t4 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.advance(2, "18 1B")

# 5. BOS #18 Mitch Moreland (X - X - 28)
t4.new_ab()
t4.pitch_list("f b b s")
t4.hit(1)

# 6. BOS #11 Rafael Devers (X - 28 - 18)
t4.new_ab()
t4.pitch_list("f b s s")
t4.out("K")

# 7. BOS #36 Eduardo Núñez (X - 28 - 18)
t4.new_ab()
t4.pitch_list("b")
t4.out("(F)P3")

# 8. BOS #3  Sandy León (X - 28 - 18)
t4.new_ab()
t4.pitch_list("f")
t4.out("F9")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
b4.new_ab()
b4.pitch_list("b c f c")
b4.out("!K")

# 2. MIN #20 Eddie Rosario (X - X - X)
b4.new_ab()
b4.pitch_list("c c b f c")
b4.out("!K")

# 3. MIN #5  Eduardo Escobar (X - X - X)
b4.new_ab()
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: MIN #17 José Berríos
t5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F9")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c b")
t5.reach("BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("1 c b s b 1")
t5.out("L7")

# 3. BOS #2  Xander Bogaerts (X - X - 50)
t5.new_ab()
t5.pitch_list("c f")
t5.out("G5-3")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 4. MIN #2  Brian Dozier (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("F9")

# 5. MIN #36 Robbie Grossman (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b f c")
b5.out("!K")

# 6. MIN #16 Ehire Adrianza (X - X - X)
b5.new_ab()
b5.pitch_list("f c b")
b5.hit(1)
b5.advance(2, "45 SB")

# 7. MIN #45 Taylor Motter (X - X - 16)
b5.new_ab()
b5.pitch_list("c b c 1 f f f b 1 b f b")
b5.reach("BB")

# 8. MIN #23 Mitch Garver (X - 16 - 45)
b5.new_ab()
b5.pitch_list("c")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: MIN #17 José Berríos
t6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L9")

# 5. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.out("F8")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c b b")
t6.hit(4, rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.hit(1)

# 8. BOS #3  Sandy León (X - X - 36)
t6.new_ab()
t6.pitch_list("s f 1 b f b s")
t6.out("K")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 9. MIN #24 Ryan LaMarre (X - X - X)
b6.new_ab()
b6.pitch_list("f f f b f")
b6.hit(1)
b6.advance(2, "7 HBP")
b6.advance(3, "20 FC3-6")
b6.advance(4, "5 2B")

# 1. MIN #7  Joe Mauer (X - X - 24)
b6.new_ab()
b6.reach("HBP")
b6.thrown_out(2, "20 FC3-6", 1, 41)

# 2. MIN #20 Eddie Rosario (X - 24 - 7)
b6.new_ab()
b6.pitch_list("s s f")
b6.reach("FC3-6")
b6.advance(4, "5 2B")

# 3. MIN #5  Eduardo Escobar (24 - X - 20)
b6.new_ab()
b6.pitch_list("b f")
b6.hit(2, rbis=2)

# 4. MIN #2  Brian Dozier (X - 5 - X)
b6.new_ab()
b6.pitch_list("s f b b")
b6.out("G5-3")

# 5. MIN #36 Robbie Grossman (X - 5 - X)
b6.new_ab()
b6.pitch_list("c f f f t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: MIN #17 José Berríos
t7 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b c c f b b f s")
t7.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.reach("HBP")
t7.advance(2, "16 SB")
t7.advance(3, "2 G5-3")

# Pitching change (MIN): #39 Trevor Hildenberger replaces #17 José Berríos
t7.pitching_substitution(39)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")
t7.advance(2, "2 G5-3")

# 3. BOS #2  Xander Bogaerts (X - 50 - 16)
t7.new_ab()
t7.pitch_list("b c b f b")
t7.out("G5-3")

# 4. BOS #28 J.D. Martinez (50 - 16 - X)
t7.new_ab()
t7.pitch_list("s b c s")
t7.out("K")


# Bot 7th
# Pitching: BOS #41 Chris Sale
b7 = game.new_inning()

# 6. MIN #16 Ehire Adrianza (X - X - X)
b7.new_ab()
b7.pitch_list("c f b f b c")
b7.out("!K")

# 7. MIN #45 Taylor Motter (X - X - X)
b7.new_ab()
b7.pitch_list("c c b b s")
b7.out("K")

# 8. MIN #23 Mitch Garver (X - X - X)
b7.new_ab()
b7.pitch_list("c s")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: MIN #32 Zach Duke
t8 = game.new_inning()

# Pitching change (MIN): #32 Zach Duke replaces #39 Trevor Hildenberger
t8.pitching_substitution(32)

# 5. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b c f b")
t8.out("F7")

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.advance(2, "36 G5-3")
t8.advance(4, "3 1B")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t8.new_ab()
t8.pitch_list("b")
t8.out("G5-3")

# 8. BOS #3  Sandy León (X - 11 - X)
t8.new_ab()
t8.pitch_list("b f b")
t8.hit(1, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t8.new_ab()
t8.pitch_list("s b b b")
t8.out("G4-3")


# Bot 8th
# Pitching: BOS #63 Robby Scott
b8 = game.new_inning()

# Pitching change (BOS): #63 Robby Scott replaces #41 Chris Sale
b8.pitching_substitution(63)

# 9. MIN #24 Ryan LaMarre (X - X - X)
b8.new_ab()
b8.pitch_list("b b f f b b")
b8.reach("BB")
b8.advance(2, "7 HBP")
b8.advance(4, "5 2B")

# 1. MIN #7  Joe Mauer (X - X - 24)
b8.new_ab()
b8.pitch_list("c l f b b 1")
b8.reach("HBP")
b8.advance(3, "5 2B")
b8.advance(4, "5 E8")

# 2. MIN #20 Eddie Rosario (X - 24 - 7)
b8.new_ab()
b8.pitch_list("s b b c f")
b8.out("F8")

# Pitching change (BOS): #56 Joe Kelly replaces #63 Robby Scott
b8.pitching_substitution(56)

# 3. MIN #5  Eduardo Escobar (X - 24 - 7)
b8.new_ab()
b8.pitch_list("f b b f")
b8.hit(2, rbis=1)
b8.error(8)
b8.advance(3, "E8")
b8.advance(4, "36 3B")

# 4. MIN #2  Brian Dozier (5 - X - X)
b8.new_ab()
b8.pitch_list("c d b f b b")
b8.reach("BB")
b8.advance(4, "36 3B")

# 5. MIN #36 Robbie Grossman (5 - X - 2)
b8.new_ab()
b8.pitch_list("b c")
b8.hit(3, rbis=2)
b8.thrown_out(4, "16 DP8-2", 3, 76)

# Pitching change (BOS): #76 Hector Velázquez replaces #56 Joe Kelly
b8.pitching_substitution(76)

# 6. MIN #16 Ehire Adrianza (36 - X - X)
b8.new_ab()
b8.pitch_list("b f b d")
b8.out("DP8-2")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: MIN #56 Fernando Rodney
t9 = game.new_inning()

# Pitching change (MIN): #56 Fernando Rodney replaces #32 Zach Duke
t9.pitching_substitution(56)

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f b f s")
t9.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("b c s b b c")
t9.out("!K")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("f b b")
t9.hit(1)
t9.advance(2, "28 DI")

# 4. BOS #28 J.D. Martinez (X - X - 2)
t9.new_ab()
t9.pitch_list("s s f b s")
t9.out("K")

# Winning team: MIN
# WP: MIN #32 Zach Duke
game.winning_pitcher(32)

# Loser team: BOS
# LP: BOS #63 Robby Scott
game.losing_pitcher(63, is_away_team=True)

# print(game)
game.generate_scorecard()
