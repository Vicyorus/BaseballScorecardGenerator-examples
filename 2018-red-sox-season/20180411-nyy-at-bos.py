import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-04-11
# https://www.baseball-reference.com/boxes/BOS/BOS201804110.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/04/11/529582/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-11 19:10-23:09",
        "at": "Fenway Park, Boston, MA",
        "att": "32,400",
        "temp": "42F, Cloudy",
        "wind": "13mph, R To L",
        "away": {
            "team": "New York Yankees",
            "starter": 19,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                99: "Aaron Judge",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                24: "Gary Sánchez",
                14: "Neil Walker",
                26: "Tyler Austin",
                12: "Tyler Wade",
                41: "Miguel Andujar",
                # Starting pitcher
                19: "Masahiro Tanaka",
                # Bench
                28: "Austin Romine",
                25: "Shane Robinson",
                74: "Ronald Torreyes",
                # Bullpen
                68: "Dellin Betances",
                40: "Luis Severino",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                55: "Sonny Gray",
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
                [11, "8"],
                [99, "9"],
                [27, "7"],
                [18, "6"],
                [24, "2"],
                [14, "3"],
                [26, "0"],
                [12, "4"],
                [41, "5"],
            ],
            "bench": [
                [28, "C"],
                [25, "CF"],
                [74, "SS"],
            ],
            "bullpen": [68, 40, 45, 65, 55, 43, 57, 48, 85, 47, 30, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                11: "Rafael Devers",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                12: "Brock Holt",
                # Starting pitcher
                24: "David Price",
                # Bench
                5: "Tzu-Wei Lin",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 61, 66],
            "lineup": [
                [50, "9"],
                [11, "5"],
                [13, "0"],
                [28, "7"],
                [18, "3"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
                [12, "6"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [16, "LF"],
                [3, "C"],
            ],
            "bullpen": [57, 39, 22, 41, 61, 66, 37, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Hunter Wendelstedt",
            "1B": "Chris Guccione",
            "2B": "David Rackley",
            "3B": "Larry Vanover",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c")
t1.hit(1)
t1.advance(2, "99 BB")
t1.advance(4, "27 3B")

# 2. NYY #99 Aaron Judge (X - X - 11)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.advance(4, "27 3B")

# 3. NYY #27 Giancarlo Stanton (X - 11 - 99)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b")
t1.hit(3, rbis=2)
t1.advance(4, "24 HR")

# 4. NYY #18 Didi Gregorius (27 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b b b")
t1.out("P3")

# 5. NYY #24 Gary Sánchez (27 - X - X)
t1.new_ab(is_risp=True)
t1.hit(4, rbis=2)

# 6. NYY #14 Neil Walker (X - X - X)
t1.new_ab()
t1.pitch_list("b c b s f")
t1.out("G6-3")

# 7. NYY #26 Tyler Austin (X - X - X)
t1.new_ab()
t1.pitch_list("s b b b b")
t1.reach("BB")

# 8. NYY #12 Tyler Wade (X - X - 26)
t1.new_ab()
t1.pitch_list("b c b s s")
t1.out("K")


# Bot 1st
# Pitching: NYY #19 Masahiro Tanaka
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("P5")

# 2. BOS #11 Rafael Devers (X - X - X)
b1.new_ab()
b1.pitch_list("c f b b")
b1.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b1.new_ab()
b1.hit(4)

# 4. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(1)
b1.advance(2, "18 WP")

# 5. BOS #18 Mitch Moreland (X - X - 28)
b1.new_ab(is_risp=True)
b1.pitch_list("b s c b b b")
b1.wp()
b1.reach("BB")

# 6. BOS #36 Eduardo Núñez (X - 28 - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("b c s d s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #66 Bobby Poyner
t2 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #24 David Price
t2.pitching_substitution(66)

# 9. NYY #41 Miguel Andujar (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("G1-3")

# 1. NYY #11 Brett Gardner (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b b b")
t2.reach("BB")
t2.advance(2, "99 1B")

# 2. NYY #99 Aaron Judge (X - X - 11)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)

# 3. NYY #27 Giancarlo Stanton (X - 11 - 99)
t2.new_ab(is_risp=True)
t2.pitch_list("c s f f f s")
t2.out("K")

# 4. NYY #18 Didi Gregorius (X - 11 - 99)
t2.new_ab(is_risp=True)
t2.pitch_list("f t f d b")
t2.out("G6-3")


# Bot 2nd
# Pitching: NYY #19 Masahiro Tanaka
b2 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.out("F8")

# 8. BOS #7  Christian Vázquez (X - X - X)
b2.new_ab()
b2.pitch_list("c f f s")
b2.out("K")

# 9. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #66 Bobby Poyner
t3 = game.new_inning()

# 5. NYY #24 Gary Sánchez (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(2)
t3.advance(3, "14 1B")
t3.advance(4, "26 1B")

# 6. NYY #14 Neil Walker (X - 24 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b b f")
t3.hit(1)
t3.advance(2, "26 1B")
t3.advance(3, "12 FC5-6")

# 7. NYY #26 Tyler Austin (24 - X - 14)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.hit(1, rbis=1)
t3.thrown_out(2, "12 FC5-6", 1, 66)

# 8. NYY #12 Tyler Wade (X - 14 - 26)
t3.new_ab(is_risp=True)
t3.reach("FC5-6")
t3.thrown_out(1, "41 DP3", 3, 66)

# 9. NYY #41 Miguel Andujar (14 - X - 12)
t3.new_ab(is_risp=True)
t3.pitch_list("c f")
t3.out("DP3")


# Bot 3rd
# Pitching: NYY #19 Masahiro Tanaka
b3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.out("G6-3")

# 2. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G3-1")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b3.new_ab()
b3.out("L5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #37 Heath Hembree
t4 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #66 Bobby Poyner
t4.pitching_substitution(37)

# 1. NYY #11 Brett Gardner (X - X - X)
t4.new_ab()
t4.pitch_list("c b f f")
t4.hit(1)
t4.advance(2, "99 1B")
t4.advance(3, "27 F7")
t4.advance(4, "18 SF7")

# 2. NYY #99 Aaron Judge (X - X - 11)
t4.new_ab()
t4.pitch_list("s d b d s f 1 f 1")
t4.hit(1)
t4.advance(4, "24 HR")

# 3. NYY #27 Giancarlo Stanton (X - 11 - 99)
t4.new_ab(is_risp=True)
t4.pitch_list("b c c")
t4.out("F7")

# 4. NYY #18 Didi Gregorius (11 - X - 99)
t4.new_ab(is_risp=True)
t4.pitch_list("f f")
t4.out("SF7", rbis=1)

# 5. NYY #24 Gary Sánchez (X - X - 99)
t4.new_ab()
t4.pitch_list("b 1")
t4.hit(4, rbis=2)

# 6. NYY #14 Neil Walker (X - X - X)
t4.new_ab()
t4.pitch_list("b f s s")
t4.out("K")


# Bot 4th
# Pitching: NYY #19 Masahiro Tanaka
b4 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c s s")
b4.out("K")

# 5. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.out("G6-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #37 Heath Hembree
t5 = game.new_inning()

# 7. NYY #26 Tyler Austin (X - X - X)
t5.new_ab()
t5.pitch_list("c b c s")
t5.out("K")

# 8. NYY #12 Tyler Wade (X - X - X)
t5.new_ab()
t5.pitch_list("f f b f")
t5.out("F8")

# 9. NYY #41 Miguel Andujar (X - X - X)
t5.new_ab()
t5.pitch_list("s")
t5.out("G5-3")


# Bot 5th
# Pitching: NYY #19 Masahiro Tanaka
b5 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b b f")
b5.hit(1)
b5.advance(2, "12 1B")
b5.advance(4, "50 2B")

# 8. BOS #7  Christian Vázquez (X - X - 19)
b5.new_ab()
b5.pitch_list("d c")
b5.out("F9")

# 9. BOS #12 Brock Holt (X - X - 19)
b5.new_ab()
b5.pitch_list("c f")
b5.hit(1)
b5.advance(3, "50 2B")
b5.advance(4, "28 HR")

# 1. BOS #50 Mookie Betts (X - 19 - 12)
b5.new_ab(is_risp=True)
b5.pitch_list("c s d b")
b5.hit(2, rbis=1)
b5.advance(4, "28 HR")

# 2. BOS #11 Rafael Devers (12 - 50 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s d b b s")
b5.out("F7")

# 3. BOS #13 Hanley Ramirez (12 - 50 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b b d")
b5.reach("BB")
b5.advance(4, "28 HR")

# 4. BOS #28 J.D. Martinez (12 - 50 - 13)
b5.new_ab(is_risp=True)
b5.hit(4, rbis=4)

# 5. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(2)

# 6. BOS #36 Eduardo Núñez (X - 18 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f d f b f")
b5.out("P3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #32 Matt Barnes
t6 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
t6.pitching_substitution(32)

# 1. NYY #11 Brett Gardner (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b b")
t6.reach("BB")
t6.error(2)
t6.advance(2, "99 SB")
t6.advance(3, "99 E2")
t6.advance(4, "27 1B")

# 2. NYY #99 Aaron Judge (X - X - 11)
t6.new_ab(is_risp=True)
t6.pitch_list("b s 1 b c c")
t6.out("!K")

# 3. NYY #27 Giancarlo Stanton (11 - X - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.hit(1, rbis=1)
t6.advance(2, "18 WP")
t6.advance(3, "18 WP")
t6.advance(4, "18 SF8")

# 4. NYY #18 Didi Gregorius (X - X - 27)
t6.new_ab(is_risp=True)
t6.pitch_list("c b b b")
t6.wp()
t6.wp()
t6.out("SF8", rbis=1)

# 5. NYY #24 Gary Sánchez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G5-3")


# Bot 6th
# Pitching: NYY #57 Chad Green
b6 = game.new_inning()

# Pitching change (NYY): #57 Chad Green replaces #19 Masahiro Tanaka
b6.pitching_substitution(57)

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.thrown_out(2, "7 FC3-6", 1, 57)

# 8. BOS #7  Christian Vázquez (X - X - 19)
b6.new_ab()
b6.pitch_list("f c f b f")
b6.reach("FC3-6")
b6.thrown_out(2, "12 DP6-4-3", 2, 57)

# 9. BOS #12 Brock Holt (X - X - 7)
b6.new_ab()
b6.pitch_list("b b f f f f")
b6.out("DP6-4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
t7.pitching_substitution(56)

# 6. NYY #14 Neil Walker (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G5-3")

# 7. NYY #26 Tyler Austin (X - X - X)
t7.new_ab()
t7.pitch_list("s b b")
t7.reach("HBP")
# Offensive change (NYY): Pinch-runner #25 Shane Robinson replaces #26 Tyler Austin
t7.offensive_substitution(7, 25, "PR")
t7.atbase("PR")

# Pitching change (BOS): #61 Brian Johnson replaces #56 Joe Kelly
t7.pitching_substitution(61)

# 8. NYY #12 Tyler Wade (X - X - 26)
t7.new_ab()
t7.pitch_list("s b s 1 c")
t7.out("!K")

# 9. NYY #41 Miguel Andujar (X - X - 25)
t7.new_ab()
t7.pitch_list("b f b c f")
t7.out("P5")


# Bot 7th
# Pitching: NYY #57 Chad Green
b7 = game.new_inning()

# Defensive switch (NYY): #25 Shane Robinson moves to DH
b7.defensive_switch(25, "0")

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b")
b7.out("G6-3")

# 2. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("c s b s")
b7.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b7.new_ab()
b7.pitch_list("b c s b f f")
b7.out("L9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #61 Brian Johnson
t8 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t8.new_ab()
t8.pitch_list("f b c b c")
t8.out("!K")

# 2. NYY #99 Aaron Judge (X - X - X)
t8.new_ab()
t8.pitch_list("f b s c")
t8.out("!K")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
t8.new_ab()
t8.pitch_list("c s b")
t8.hit(1)

# 4. NYY #18 Didi Gregorius (X - X - 27)
t8.new_ab()
t8.pitch_list("f b c b")
t8.out("F8")


# Bot 8th
# Pitching: NYY #30 David Robertson
b8 = game.new_inning()

# Pitching change (NYY): #30 David Robertson replaces #57 Chad Green
b8.pitching_substitution(30)

# Defensive change (NYY): #74 Ronald Torreyes replaces #41 Miguel Andujar (3B), playing 3B, batting 9th
b8.defensive_substitution(9, 74, "5")

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b c s f b b c")
b8.out("!K")

# 5. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f b")
b8.out("F8")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b8.new_ab()
b8.pitch_list("s b b c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #39 Carson Smith
t9 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #61 Brian Johnson
t9.pitching_substitution(39)

# 5. NYY #24 Gary Sánchez (X - X - X)
t9.new_ab()
t9.pitch_list("b b c")
t9.out("G3-1")

# 6. NYY #14 Neil Walker (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.out("G6-3")

# 7. NYY #25 Shane Robinson (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c b")
t9.reach("BB")
t9.advance(2, "12 SB")

# 8. NYY #12 Tyler Wade (X - X - 25)
t9.new_ab(is_risp=True)
t9.pitch_list("b f b c c")
t9.out("!K")


# Bot 9th
# Pitching: NYY #54 Aroldis Chapman
b9 = game.new_inning()

# Pitching change (NYY): #54 Aroldis Chapman replaces #30 David Robertson
b9.pitching_substitution(54)

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.hit(1)
b9.advance(3, "7 2B")
b9.advance(4, "11 WP")

# 8. BOS #7  Christian Vázquez (X - X - 19)
b9.new_ab()
b9.pitch_list("1 b 1 f b b c")
b9.hit(2)
b9.advance(3, "11 WP")

# Offensive change (BOS): Pinch-hitter #3 Sandy León replaces #12 Brock Holt, batting 9th
b9.offensive_substitution(9, 3, "PH")

# 9. BOS #3  Sandy León (19 - 7 - X)
b9.new_ab(is_risp=True)
b9.out("F9")

# 1. BOS #50 Mookie Betts (19 - 7 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c d d b c s")
b9.out("K")

# 2. BOS #11 Rafael Devers (19 - 7 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b f b s s")
b9.wp()
b9.out("K")

# Winning team: NYY
# WP: NYY #19 Masahiro Tanaka
game.winning_pitcher(19, is_away_team=True)

# Loser team: BOS
# LP: BOS #24 David Price
game.losing_pitcher(24)

# print(game)
game.generate_scorecard()
