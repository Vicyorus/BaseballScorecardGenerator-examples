import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-04-10
# https://www.baseball-reference.com/boxes/BOS/BOS201804100.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/04/10/529568/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-10 19:10-22:21",
        "at": "Fenway Park, Boston, MA",
        "att": "32,357",
        "temp": "38F, Cloudy",
        "wind": "5mph, L To R",
        "away": {
            "team": "New York Yankees",
            "starter": 40,
            "roster": {
                # Lineup
                14: "Neil Walker",
                99: "Aaron Judge",
                27: "Giancarlo Stanton",
                24: "Gary Sánchez",
                18: "Didi Gregorius",
                26: "Tyler Austin",
                41: "Miguel Andujar",
                28: "Austin Romine",
                25: "Shane Robinson",
                # Starting pitcher
                40: "Luis Severino",
                # Bench
                11: "Brett Gardner",
                12: "Tyler Wade",
                74: "Ronald Torreyes",
                # Bullpen
                68: "Dellin Betances",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                55: "Sonny Gray",
                19: "Masahiro Tanaka",
                43: "Adam Warren",
                57: "Chad Green",
                48: "Tommy Kahnle",
                85: "Luis Cessa",
                47: "Jordan Montgomery",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [45, 47, 54],
            "lineup": [
                [14, "4"],
                [99, "9"],
                [27, "7"],
                [24, "0"],
                [18, "6"],
                [26, "3"],
                [41, "5"],
                [28, "2"],
                [25, "8"],
            ],
            "bench": [
                [11, "LF"],
                [12, "3B"],
                [74, "SS"],
            ],
            "bullpen": [68, 45, 65, 55, 19, 43, 57, 48, 85, 47, 30, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
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
                41: "Chris Sale",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 61, 66, 24],
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
            "bullpen": [57, 39, 22, 61, 66, 37, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Larry Vanover",
            "1B": "Hunter Wendelstedt",
            "2B": "Chris Guccione",
            "3B": "David Rackley",
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
# Pitching: BOS #41 Chris Sale
t1 = game.new_inning()

# 1. NYY #14 Neil Walker (X - X - X)
t1.new_ab()
t1.pitch_list("b f b b")
t1.out("(F)P3")

# 2. NYY #99 Aaron Judge (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)
t1.thrown_out(2, "24 FC5-4", 3, 41)

# 3. NYY #27 Giancarlo Stanton (X - X - 99)
t1.new_ab()
t1.pitch_list("c s s")
t1.out("K")

# 4. NYY #24 Gary Sánchez (X - X - 99)
t1.new_ab()
t1.pitch_list("c b")
t1.reach("FC5-4")


# Bot 1st
# Pitching: NYY #40 Luis Severino
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(2)
b1.advance(4, "13 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b1.new_ab()
b1.pitch_list("d c d b b")
b1.reach("BB")
b1.advance(3, "13 1B")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(1, rbis=1)
b1.advance(2, "11 BB")

# 4. BOS #28 J.D. Martinez (16 - X - 13)
b1.new_ab()
b1.pitch_list("s f s")
b1.out("K")

# 5. BOS #11 Rafael Devers (16 - X - 13)
b1.new_ab()
b1.pitch_list("f b 1 f f b b d")
b1.reach("BB")

# 6. BOS #36 Eduardo Núñez (16 - 13 - 11)
b1.new_ab()
b1.pitch_list("f")
b1.out("L3")

# 7. BOS #19 Jackie Bradley Jr. (16 - 13 - 11)
b1.new_ab()
b1.pitch_list("s b b s s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 5. NYY #18 Didi Gregorius (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G1")

# 6. NYY #26 Tyler Austin (X - X - X)
t2.new_ab()
t2.hit(1)

# 7. NYY #41 Miguel Andujar (X - X - 26)
t2.new_ab()
t2.pitch_list("c")
t2.out("F7")

# 8. NYY #28 Austin Romine (X - X - 26)
t2.new_ab()
t2.pitch_list("s c s")
t2.out("K")


# Bot 2nd
# Pitching: NYY #40 Luis Severino
b2 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
b2.new_ab()
b2.pitch_list("s b s f")
b2.hit(1)
b2.advance(2, "50 1B")
b2.advance(4, "16 3B")

# 9. BOS #12 Brock Holt (X - X - 7)
b2.new_ab()
b2.pitch_list("c b c b f c")
b2.out("!K")

# 1. BOS #50 Mookie Betts (X - X - 7)
b2.new_ab()
b2.pitch_list("b f f")
b2.hit(1)
b2.advance(4, "16 3B")

# 2. BOS #16 Andrew Benintendi (X - 7 - 50)
b2.new_ab()
b2.pitch_list("f b")
b2.hit(3, rbis=2)
b2.advance(4, "13 1B")

# 3. BOS #13 Hanley Ramirez (16 - X - X)
b2.new_ab()
b2.pitch_list("b b f f")
b2.hit(1, rbis=1)
b2.error(2)
b2.advance(2, "11 SB")
b2.advance(3, "11 E2")

# 4. BOS #28 J.D. Martinez (X - X - 13)
b2.new_ab()
b2.pitch_list("b b s 1 b s")
b2.out("L9")

# 5. BOS #11 Rafael Devers (X - X - 13)
b2.new_ab()
b2.pitch_list("b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 9. NYY #25 Shane Robinson (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("P4")

# 1. NYY #14 Neil Walker (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b f f f")
t3.hit(1)
t3.advance(2, "99 1B")

# 2. NYY #99 Aaron Judge (X - X - 14)
t3.new_ab()
t3.pitch_list("s")
t3.hit(1)

# 3. NYY #27 Giancarlo Stanton (X - 14 - 99)
t3.new_ab()
t3.pitch_list("s f f s")
t3.out("K")

# 4. NYY #24 Gary Sánchez (X - 14 - 99)
t3.new_ab()
t3.pitch_list("b f f f f s")
t3.out("K")


# Bot 3rd
# Pitching: NYY #40 Luis Severino
b3 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("c b b f")
b3.out("G4-3")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("s f")
b3.out("F8")

# 8. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 5. NYY #18 Didi Gregorius (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)

# 6. NYY #26 Tyler Austin (X - X - 18)
t4.new_ab()
t4.pitch_list("b c f s")
t4.out("K")

# 7. NYY #41 Miguel Andujar (X - X - 18)
t4.new_ab()
t4.pitch_list("s s b f f s")
t4.out("K")

# 8. NYY #28 Austin Romine (X - X - 18)
t4.new_ab()
t4.pitch_list("b s b s b s")
t4.out("K")


# Bot 4th
# Pitching: NYY #40 Luis Severino
b4 = game.new_inning()

# 9. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("c s c")
b4.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("b b s b b")
b4.reach("BB")
b4.advance(3, "16 2B")
b4.advance(4, "13 SF9")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b4.new_ab()
b4.hit(2)
b4.advance(3, "13 SF9")

# 3. BOS #13 Hanley Ramirez (50 - 16 - X)
b4.new_ab()
b4.pitch_list("s")
b4.out("SF9", rbis=1)

# 4. BOS #28 J.D. Martinez (16 - X - X)
b4.new_ab()
b4.pitch_list("f s")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 9. NYY #25 Shane Robinson (X - X - X)
t5.new_ab()
t5.pitch_list("c s s")
t5.out("K2-3")

# 1. NYY #14 Neil Walker (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("L8")

# 2. NYY #99 Aaron Judge (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(4, rbis=1)

# 3. NYY #27 Giancarlo Stanton (X - X - X)
t5.new_ab()
t5.pitch_list("s b")
t5.hit(1)

# 4. NYY #24 Gary Sánchez (X - X - 27)
t5.new_ab()
t5.pitch_list("b s")
t5.out("(F)P2")


# Bot 5th
# Pitching: NYY #40 Luis Severino
b5 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("b s b f c")
b5.out("!K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.out("F8")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.hit(1)

# 8. BOS #7  Christian Vázquez (X - X - 19)
b5.new_ab()
b5.pitch_list("1 s f b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 Chris Sale
t6 = game.new_inning()

# 5. NYY #18 Didi Gregorius (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.hit(1)

# 6. NYY #26 Tyler Austin (X - X - 18)
t6.new_ab()
t6.pitch_list("s c d")
t6.out("F7")

# 7. NYY #41 Miguel Andujar (X - X - 18)
t6.new_ab()
t6.pitch_list("1")
t6.out("F7")

# 8. NYY #28 Austin Romine (X - X - 18)
t6.new_ab()
t6.pitch_list("b b")
t6.out("P2")


# Bot 6th
# Pitching: NYY #48 Tommy Kahnle
b6 = game.new_inning()

# Pitching change (NYY): #48 Tommy Kahnle replaces #40 Luis Severino
b6.pitching_substitution(48)

# 9. BOS #12 Brock Holt (X - X - X)
b6.new_ab()
b6.out("G3-1")

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(2)
b6.advance(3, "13 BB")
b6.advance(4, "28 2B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b6.new_ab()
b6.pitch_list("b b d d")
b6.reach("BB")
b6.advance(2, "13 BB")
b6.advance(4, "28 2B")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
b6.new_ab()
b6.pitch_list("b b s b b")
b6.reach("BB")
b6.advance(3, "28 2B")
b6.advance(4, "11 SF8")

# 4. BOS #28 J.D. Martinez (50 - 16 - 13)
b6.new_ab()
b6.pitch_list("c b s f")
b6.hit(2, rbis=2)
b6.advance(3, "19 HBP")
b6.advance("U", "7 E5")

# 5. BOS #11 Rafael Devers (13 - 28 - X)
b6.new_ab()
b6.out("SF8", rbis=1)

# 6. BOS #36 Eduardo Núñez (X - 28 - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "19 HBP")
b6.advance(3, "7 E5")
b6.advance("U", "12 BB")

# Pitching change (NYY): #45 Chasen Shreve replaces #48 Tommy Kahnle
b6.pitching_substitution(45)

# 7. BOS #19 Jackie Bradley Jr. (X - 28 - 36)
b6.new_ab()
b6.reach("HBP")
b6.advance(2, "7 E5")
b6.advance(3, "12 BB")
b6.advance("U", "50 HR")

# 8. BOS #7  Christian Vázquez (28 - 36 - 19)
b6.new_ab()
b6.pitch_list("c")
b6.error(5)
b6.reach("E5")
b6.advance(2, "12 BB")
b6.advance("U", "50 HR")

# 9. BOS #12 Brock Holt (36 - 19 - 7)
b6.new_ab()
b6.pitch_list("c b b d b")
b6.reach("BB", rbis=1)
b6.advance("U", "50 HR")

# 1. BOS #50 Mookie Betts (19 - 7 - 12)
b6.new_ab()
b6.pitch_list("b c b")
b6.hit("U", rbis=4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("f c f b b b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #41 Chris Sale
t7.pitching_substitution(56)

# Defensive change (BOS): #23 Blake Swihart replaces #13 Hanley Ramirez (1B), playing 1B, batting 3rd
t7.defensive_substitution(3, 23, "3")

# Defensive change (BOS): #5 Tzu-Wei Lin replaces #36 Eduardo Núñez (2B), playing SS, batting 6th
t7.defensive_substitution(6, 5, "6")

# Defensive switch (BOS): #12 Brock Holt moves to 2B
t7.defensive_switch(12, "4")

# 9. NYY #25 Shane Robinson (X - X - X)
t7.new_ab()
t7.pitch_list("b c b c b f f")
t7.hit(1)
t7.thrown_out(2, "12 FC6-5", 1, 56)

# Offensive change (NYY): Pinch-hitter #12 Tyler Wade replaces #14 Neil Walker, batting 1st
t7.offensive_substitution(1, 12, "PH")

# 1. NYY #12 Tyler Wade (X - X - 25)
t7.new_ab()
t7.pitch_list("f b d f b")
t7.reach("FC6-5")
t7.thrown_out(2, "99 DP6-4-3", 2, 56)

# 2. NYY #99 Aaron Judge (X - X - 12)
t7.new_ab()
t7.pitch_list("b f c")
t7.out("DP6-4-3")


# Bot 7th
# Pitching: NYY #45 Chasen Shreve
b7 = game.new_inning()

# Defensive switch (NYY): #12 Tyler Wade moves to 2B
b7.defensive_switch(12, "4")

# 3. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.pitch_list("f b s s")
b7.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("c s f s")
b7.out("K")

# 5. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("c b b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #61 Brian Johnson
t8 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #56 Joe Kelly
t8.pitching_substitution(61)

# 3. NYY #27 Giancarlo Stanton (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c f")
t8.hit(2)

# 4. NYY #24 Gary Sánchez (X - 27 - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("F8")

# 5. NYY #18 Didi Gregorius (X - 27 - X)
t8.new_ab()
t8.pitch_list("b d")
t8.out("P6")

# 6. NYY #26 Tyler Austin (X - 27 - X)
t8.new_ab()
t8.out("F9")


# Bot 8th
# Pitching: NYY #85 Luis Cessa
b8 = game.new_inning()

# Pitching change (NYY): #85 Luis Cessa replaces #45 Chasen Shreve
b8.pitching_substitution(85)

# Defensive switch (NYY): #12 Tyler Wade moves to CF
b8.defensive_switch(12, "8")

# Defensive change (NYY): #74 Ronald Torreyes replaces #27 Giancarlo Stanton (LF), playing 2B, batting 3rd
b8.defensive_substitution(3, 74, "4")

# Defensive switch (NYY): #25 Shane Robinson moves to LF
b8.defensive_switch(25, "7")

# 6. BOS #5  Tzu-Wei Lin (X - X - X)
b8.new_ab()
b8.pitch_list("b b c b f t")
b8.out("KT")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("b c s")
b8.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("L3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #61 Brian Johnson
t9 = game.new_inning()

# 7. NYY #41 Miguel Andujar (X - X - X)
t9.new_ab()
t9.pitch_list("b c f f b c")
t9.out("!K")

# 8. NYY #28 Austin Romine (X - X - X)
t9.new_ab()
t9.pitch_list("b c c s")
t9.out("K2-3")

# 9. NYY #25 Shane Robinson (X - X - X)
t9.new_ab()
t9.pitch_list("f b b b b")
t9.reach("BB")

# 1. NYY #12 Tyler Wade (X - X - 25)
t9.new_ab()
t9.pitch_list("b f c d f f f")
t9.out("G3-1")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41)

# Loser team: NYY
# LP: NYY #40 Luis Severino
game.losing_pitcher(40, is_away_team=True)

# print(game)
game.generate_scorecard()
