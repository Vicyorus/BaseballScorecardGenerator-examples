import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-07-01
# https://www.baseball-reference.com/boxes/NYA/NYA201807010.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/07/01/530654/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-01 20:07-23:21",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "46,795",
        "temp": "91F, Clear",
        "wind": "6mph, Out To LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [12, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 44, 22, 41, 61, 37, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 40,
            "roster": {
                # Lineup
                31: "Aaron Hicks",
                99: "Aaron Judge",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                25: "Gleyber Torres",
                41: "Miguel Andujar",
                33: "Greg Bird",
                66: "Kyle Higashioka",
                11: "Brett Gardner",
                # Starting pitcher
                40: "Luis Severino",
                # Bench
                28: "Austin Romine",
                29: "Brandon Drury",
                14: "Neil Walker",
                # Bullpen
                68: "Dellin Betances",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                38: "Jonathan Loáisiga",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                52: "CC Sabathia",
                43: "Adam Warren",
                57: "Chad Green",
                61: "David Hale",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [45, 52, 54],
            "lineup": [
                [31, "8"],
                [99, "9"],
                [27, "0"],
                [18, "6"],
                [25, "4"],
                [41, "5"],
                [33, "3"],
                [66, "2"],
                [11, "7"],
            ],
            "bench": [
                [28, "C"],
                [29, "2B"],
                [14, "2B"],
            ],
            "bullpen": [68, 45, 65, 38, 55, 56, 52, 43, 57, 61, 30, 54],
        },
        "umpires": {
            "HP": "Fieldin Culbreth",
            "1B": "CB Bucknor",
            "2B": "Chris Conroy",
            "3B": "Brian O'Nora",
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
# Pitching: NYY #40 Luis Severino
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("f b s")
t1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("f c t")
t1.out("KT")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t1.new_ab()
t1.pitch_list("c f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f b")
b1.out("G5-3")

# 2. NYY #99 Aaron Judge (X - X - X)
b1.new_ab()
b1.pitch_list("f b b s")
b1.hit(4)

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b1.new_ab()
b1.pitch_list("b b t")
b1.hit(1)
b1.advance(3, "18 2B")
b1.advance(4, "25 HR")

# 4. NYY #18 Didi Gregorius (X - X - 27)
b1.new_ab()
b1.hit(2)
b1.advance(4, "25 HR")

# 5. NYY #25 Gleyber Torres (27 - 18 - X)
b1.new_ab(is_risp=True)
b1.hit(4, rbis=3)

# 6. NYY #41 Miguel Andujar (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G4-3")

# 7. NYY #33 Greg Bird (X - X - X)
b1.new_ab()
b1.pitch_list("b c t b")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #40 Luis Severino
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c f")
t2.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c t b f")
t2.out("G3")

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("f f b b f")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 8. NYY #66 Kyle Higashioka (X - X - X)
b2.new_ab()
b2.pitch_list("f f b c")
b2.out("!K")

# 9. NYY #11 Brett Gardner (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(4, "31 HR")

# 1. NYY #31 Aaron Hicks (X - X - 11)
b2.new_ab()
b2.pitch_list("b f")
b2.hit(4, rbis=2)

# 2. NYY #99 Aaron Judge (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.out("F9")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #40 Luis Severino
t3 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("L7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b s f s")
t3.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b b")
t3.reach("BB")
t3.advance(3, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t3.new_ab()
t3.pitch_list("1 s f f")
t3.hit(1)
t3.advance(2, "28 SB")

# 3. BOS #28 J.D. Martinez (50 - X - 16)
t3.new_ab(is_risp=True)
t3.pitch_list("b b f c b f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 4. NYY #18 Didi Gregorius (X - X - X)
b3.new_ab()
b3.pitch_list("c b f")
b3.out("G1-3")

# 5. NYY #25 Gleyber Torres (X - X - X)
b3.new_ab()
b3.pitch_list("s b c f f f f s")
b3.out("K")

# 6. NYY #41 Miguel Andujar (X - X - X)
b3.new_ab()
b3.pitch_list("c b s b f")
b3.hit(1)

# 7. NYY #33 Greg Bird (X - X - 41)
b3.new_ab()
b3.pitch_list("f b f f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #40 Luis Severino
t4 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b b")
t4.out("G4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("P6")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 8. NYY #66 Kyle Higashioka (X - X - X)
b4.new_ab()
b4.pitch_list("c f b")
b4.hit(4)

# 9. NYY #11 Brett Gardner (X - X - X)
b4.new_ab()
b4.pitch_list("c c")
b4.out("G3-1")

# 1. NYY #31 Aaron Hicks (X - X - X)
b4.new_ab()
b4.hit(4)

# Pitching change (BOS): #65 Justin Haley replaces #24 David Price
b4.pitching_substitution(65)

# 2. NYY #99 Aaron Judge (X - X - X)
b4.new_ab()
b4.pitch_list("s")
b4.hit(1)
b4.advance(3, "27 2B")
b4.advance(4, "18 SF7")

# 3. NYY #27 Giancarlo Stanton (X - X - 99)
b4.new_ab()
b4.hit(2)

# 4. NYY #18 Didi Gregorius (99 - 27 - X)
b4.new_ab(is_risp=True)
b4.out("SF7", rbis=1)

# 5. NYY #25 Gleyber Torres (X - 27 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #40 Luis Severino
t5 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G5-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c f")
t5.out("F8")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("s b s b b f b")
t5.reach("BB")

# 1. BOS #50 Mookie Betts (X - X - 19)
t5.new_ab()
t5.pitch_list("c b f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #65 Justin Haley
b5 = game.new_inning()

# 6. NYY #41 Miguel Andujar (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.advance(2, "33 G6-3")
b5.advance(3, "66 F9")

# 7. NYY #33 Greg Bird (X - X - 41)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")

# 8. NYY #66 Kyle Higashioka (X - 41 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c b s")
b5.out("F9")

# 9. NYY #11 Brett Gardner (41 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b c f b f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #40 Luis Severino
t6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G5-3")

# 4. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("c b f")
t6.hit(1)

# 5. BOS #2  Xander Bogaerts (X - X - 18)
t6.new_ab()
t6.pitch_list("s s s")
t6.out("K")


# Bot 6th
# Pitching: BOS #65 Justin Haley
b6 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
b6.new_ab()
b6.pitch_list("f b c b b b")
b6.reach("BB")
b6.advance(2, "99 1B")
b6.advance(3, "14 FC4-6")

# 2. NYY #99 Aaron Judge (X - X - 31)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)
b6.thrown_out(2, "14 FC4-6", 2, 65)

# 3. NYY #27 Giancarlo Stanton (X - 31 - 99)
b6.new_ab(is_risp=True)
b6.pitch_list("s b b c f")
b6.out("IF3")

# Offensive change (NYY): Pinch-hitter #14 Neil Walker replaces #18 Didi Gregorius, batting 4th
b6.offensive_substitution(4, 14, "PH")

# 4. NYY #14 Neil Walker (X - 31 - 99)
b6.new_ab(is_risp=True)
b6.reach("FC4-6")
b6.advance(2, "25 BB")

# 5. NYY #25 Gleyber Torres (31 - X - 14)
b6.new_ab(is_risp=True)
b6.pitch_list("b f d b b")
b6.reach("BB")
b6.thrown_out(2, "41 FC5-4", 3, 65)

# 6. NYY #41 Miguel Andujar (31 - 14 - 25)
b6.new_ab(is_risp=True)
b6.reach("FC5-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #40 Luis Severino
t7 = game.new_inning()

# Defensive switch (NYY): #14 Neil Walker moves to 2B
t7.defensive_switch(14, "4")

# Defensive switch (NYY): #25 Gleyber Torres moves to SS
t7.defensive_switch(25, "6")

# 6. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("G6-3")

# 7. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("f f b f")
t7.out("G4-3")

# Pitching change (NYY): #30 David Robertson replaces #40 Luis Severino
t7.pitching_substitution(30)

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.out("L8")


# Bot 7th
# Pitching: BOS #44 Brandon Workman
b7 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #65 Justin Haley
b7.pitching_substitution(44)

# Defensive change (BOS): #25 Steve Pearce replaces #50 Mookie Betts (RF), playing RF, batting 1st
b7.defensive_substitution(1, 25, "9")

# Defensive change (BOS): #23 Blake Swihart replaces #2 Xander Bogaerts (SS), playing 2B, batting 5th
b7.defensive_substitution(5, 23, "4")

# Defensive switch (BOS): #12 Brock Holt moves to SS
b7.defensive_switch(12, "6")

# 7. NYY #33 Greg Bird (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("P5")

# 8. NYY #66 Kyle Higashioka (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("F7")

# 9. NYY #11 Brett Gardner (X - X - X)
b7.new_ab()
b7.pitch_list("c b b c b")
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #30 David Robertson
t8 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b b s")
t8.out("K")

# 1. BOS #25 Steve Pearce (X - X - X)
t8.new_ab()
t8.pitch_list("c f b t")
t8.out("KT")

# Pitching change (NYY): #68 Dellin Betances replaces #30 David Robertson
t8.pitching_substitution(68)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("f b c b f")
t8.out("G3-1")


# Bot 8th
# Pitching: BOS #76 Hector Velázquez
b8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #44 Brandon Workman
b8.pitching_substitution(76)

# 1. NYY #31 Aaron Hicks (X - X - X)
b8.new_ab()
b8.pitch_list("b c c f")
b8.hit(4)

# 2. NYY #99 Aaron Judge (X - X - X)
b8.new_ab()
b8.pitch_list("c b c b b f b")
b8.reach("BB")
b8.advance(2, "29 1B")
b8.advance(4, "14 1B")

# Offensive change (NYY): Pinch-hitter #29 Brandon Drury replaces #27 Giancarlo Stanton, batting 3rd
b8.offensive_substitution(3, 29, "PH")

# 3. NYY #29 Brandon Drury (X - X - 99)
b8.new_ab()
b8.hit(1)
b8.advance(2, "14 1B")

# 4. NYY #14 Neil Walker (X - 99 - 29)
b8.new_ab(is_risp=True)
b8.pitch_list("c")
b8.hit(1, rbis=1)
b8.thrown_out(2, "41 DP5-4-3", 2, 76)

# 5. NYY #25 Gleyber Torres (X - 29 - 14)
b8.new_ab(is_risp=True)
b8.pitch_list("d f b f")
b8.out("F8")

# 6. NYY #41 Miguel Andujar (X - 29 - 14)
b8.new_ab(is_risp=True)
b8.pitch_list("b b f")
b8.out("DP5-4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #68 Dellin Betances
t9 = game.new_inning()

# Defensive switch (NYY): #29 Brandon Drury moves to DH
t9.defensive_switch(29, "0")

# 3. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("s s t")
t9.out("KT")

# Pitching change (NYY): #54 Aroldis Chapman replaces #68 Dellin Betances
t9.pitching_substitution(54)

# Offensive change (BOS): Pinch-hitter #3 Sandy León replaces #18 Mitch Moreland, batting 4th
t9.offensive_substitution(4, 3, "PH")

# 4. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(2)
t9.advance(3, "23 1B")
t9.advance(4, "11 FC5-4")

# 5. BOS #23 Blake Swihart (X - 3 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b f b c f b")
t9.hit(1)
t9.thrown_out(2, "11 FC5-4", 2, 54)

# 6. BOS #11 Rafael Devers (3 - X - 23)
t9.new_ab(is_risp=True)
t9.pitch_list("f")
t9.reach("FC5-4", rbis=1)
t9.thrown_out(2, "12 FC6", 3, 54)

# 7. BOS #12 Brock Holt (X - X - 11)
t9.new_ab()
t9.pitch_list("c b c")
t9.reach("FC6")

# Winning team: NYY
# WP: NYY #40 Luis Severino
game.winning_pitcher(40)

# Loser team: BOS
# LP: BOS #24 David Price
game.losing_pitcher(24, is_away_team=True)

# print(game)
game.generate_scorecard()
