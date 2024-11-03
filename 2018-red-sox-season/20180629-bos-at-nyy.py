import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-06-29
# https://www.baseball-reference.com/boxes/NYA/NYA201806290.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/06/29/530624/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-29 19:09-21:50",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "47,120",
        "temp": "90F, Clear",
        "wind": "12mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                25: "Steve Pearce",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                44: "Brandon Workman",
                22: "Rick Porcello",
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
                [25, "3"],
                [2, "6"],
                [36, "4"],
                [11, "5"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [44, 22, 41, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 52,
            "roster": {
                # Lineup
                31: "Aaron Hicks",
                99: "Aaron Judge",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                25: "Gleyber Torres",
                41: "Miguel Andujar",
                33: "Greg Bird",
                28: "Austin Romine",
                11: "Brett Gardner",
                # Starting pitcher
                52: "CC Sabathia",
                # Bench
                29: "Brandon Drury",
                66: "Kyle Higashioka",
                14: "Neil Walker",
                # Bullpen
                68: "Dellin Betances",
                40: "Luis Severino",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                61: "Giovanny Gallegos",
                38: "Jonathan Loáisiga",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                43: "Adam Warren",
                57: "Chad Green",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [52, 45, 54],
            "lineup": [
                [31, "8"],
                [99, "9"],
                [27, "0"],
                [18, "6"],
                [25, "4"],
                [41, "5"],
                [33, "3"],
                [28, "2"],
                [11, "7"],
            ],
            "bench": [
                [29, "2B"],
                [66, "C"],
                [14, "2B"],
            ],
            "bullpen": [68, 40, 45, 65, 61, 38, 55, 56, 43, 57, 30, 54],
        },
        "umpires": {
            "HP": "Chris Conroy",
            "1B": "Brian O'Nora",
            "2B": "Fieldin Culbreth",
            "3B": "CB Bucknor",
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
# Pitching: NYY #52 CC Sabathia
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b c s t")
t1.out("KT")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("f s b")
t1.out("G5-3")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("F8")

# 2. NYY #99 Aaron Judge (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("L8")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b1.new_ab()
b1.pitch_list("b s b f f b b")
b1.reach("BB")

# 4. NYY #18 Didi Gregorius (X - X - 27)
b1.new_ab()
b1.pitch_list("b f b f")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #52 CC Sabathia
t2 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
t2.new_ab()
t2.hit(2)
t2.advance(3, "2 F9")

# 5. BOS #2  Xander Bogaerts (X - 25 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b c b")
t2.out("F9")

# 6. BOS #36 Eduardo Núñez (25 - X - X)
t2.new_ab(is_risp=True)
t2.out("(F)P3")

# 7. BOS #11 Rafael Devers (25 - X - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b")
t2.out("L8")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 5. NYY #25 Gleyber Torres (X - X - X)
b2.new_ab()
b2.hit(3)
b2.advance(4, "41 1B")

# 6. NYY #41 Miguel Andujar (25 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.hit(1, rbis=1)
b2.thrown_out(2, "28 DP6-4-3", 2, 57)

# 7. NYY #33 Greg Bird (X - X - 41)
b2.new_ab()
b2.pitch_list("f c b c")
b2.out("!K")

# 8. NYY #28 Austin Romine (X - X - 41)
b2.new_ab()
b2.pitch_list("b f")
b2.out("DP6-4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #52 CC Sabathia
t3 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("s s")
t3.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s c")
t3.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b c b f")
t3.hit(1)
t3.advance(2, "16 SB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t3.new_ab(is_risp=True)
t3.pitch_list("b 1 c b b b")
t3.reach("BB")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
t3.new_ab(is_risp=True)
t3.out("F8")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 9. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.pitch_list("c c b b b")
b3.out("G5-3")

# 1. NYY #31 Aaron Hicks (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("G5-3")

# 2. NYY #99 Aaron Judge (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c")
b3.out("L8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #52 CC Sabathia
t4 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
t4.new_ab()
t4.pitch_list("b b f")
t4.hit(1)
t4.thrown_out(2, "2 DP5-4-3", 1, 52)

# 5. BOS #2  Xander Bogaerts (X - X - 25)
t4.new_ab()
t4.pitch_list("f b s b")
t4.out("DP5-4-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)

# 7. BOS #11 Rafael Devers (X - X - 36)
t4.new_ab()
t4.pitch_list("b f")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b4.new_ab()
b4.pitch_list("c t b b b f b")
b4.reach("BB")
b4.advance(3, "18 2B")
b4.advance(4, "25 SF7")

# 4. NYY #18 Didi Gregorius (X - X - 27)
b4.new_ab()
b4.hit(2)
b4.advance(4, "41 HR")

# 5. NYY #25 Gleyber Torres (27 - 18 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b s b")
b4.out("SF7", rbis=1)

# 6. NYY #41 Miguel Andujar (X - 18 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c")
b4.hit(4, rbis=2)

# 7. NYY #33 Greg Bird (X - X - X)
b4.new_ab()
b4.pitch_list("b b f b s")
b4.hit(4)

# 8. NYY #28 Austin Romine (X - X - X)
b4.new_ab()
b4.out("G4-3")

# 9. NYY #11 Brett Gardner (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b c")
b4.hit(1)

# 1. NYY #31 Aaron Hicks (X - X - 11)
b4.new_ab()
b4.pitch_list("b b")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #52 CC Sabathia
t5 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("L7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b b c c f")
t5.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(2)
t5.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b f b")
t5.hit(2, rbis=1)
t5.advance(3, "28 SB")

# 3. BOS #28 J.D. Martinez (X - 16 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b b c")
t5.out("F9")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 2. NYY #99 Aaron Judge (X - X - X)
b5.new_ab()
b5.pitch_list("b c b b c f c")
b5.out("!K")

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b5.new_ab()
b5.pitch_list("f c b")
b5.out("G4-3")

# 4. NYY #18 Didi Gregorius (X - X - X)
b5.new_ab()
b5.pitch_list("f b")
b5.out("L5")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #52 CC Sabathia
t6 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
t6.new_ab()
t6.pitch_list("f b s b s")
t6.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.out("F8")


# Bot 6th
# Pitching: BOS #57 Eduardo Rodriguez
b6 = game.new_inning()

# 5. NYY #25 Gleyber Torres (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)

# 6. NYY #41 Miguel Andujar (X - X - 25)
b6.new_ab()
b6.pitch_list("s")
b6.out("(F)P3")

# 7. NYY #33 Greg Bird (X - X - 25)
b6.new_ab()
b6.pitch_list("b t b")
b6.out("P4")

# 8. NYY #28 Austin Romine (X - X - 25)
b6.new_ab()
b6.pitch_list("f b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #52 CC Sabathia
t7 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("c s s")
t7.out("K2-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("c f s")
t7.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.reach("HBP")

# 1. BOS #50 Mookie Betts (X - X - 19)
t7.new_ab()
t7.pitch_list("b b c b c")
t7.out("G1-3")


# Bot 7th
# Pitching: BOS #65 Justin Haley
b7 = game.new_inning()

# Pitching change (BOS): #65 Justin Haley replaces #57 Eduardo Rodriguez
b7.pitching_substitution(65)

# 9. NYY #11 Brett Gardner (X - X - X)
b7.new_ab()
b7.pitch_list("b c c f")
b7.out("G4-3")

# 1. NYY #31 Aaron Hicks (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(1)
b7.advance(4, "99 HR")

# 2. NYY #99 Aaron Judge (X - X - 31)
b7.new_ab()
b7.pitch_list("f f b b f d")
b7.hit(4, rbis=2)

# 3. NYY #27 Giancarlo Stanton (X - X - X)
b7.new_ab()
b7.pitch_list("b f f b f f f")
b7.out("F8")

# 4. NYY #18 Didi Gregorius (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #57 Chad Green
t8 = game.new_inning()

# Pitching change (NYY): #57 Chad Green replaces #52 CC Sabathia
t8.pitching_substitution(57)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("b f b f f c")
t8.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b c f")
t8.out("L9")

# 4. BOS #25 Steve Pearce (X - X - X)
t8.new_ab()
t8.pitch_list("b c f")
t8.out("F8")


# Bot 8th
# Pitching: BOS #65 Justin Haley
b8 = game.new_inning()

# 5. NYY #25 Gleyber Torres (X - X - X)
b8.new_ab()
b8.out("F9")

# 6. NYY #41 Miguel Andujar (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(1)
b8.thrown_out(2, "8-4", 2, 65)

# 7. NYY #33 Greg Bird (X - X - X)
b8.new_ab()
b8.pitch_list("b c c b b")
b8.hit(4)

# 8. NYY #28 Austin Romine (X - X - X)
b8.new_ab()
b8.pitch_list("c b f f")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #45 Chasen Shreve
t9 = game.new_inning()

# Pitching change (NYY): #45 Chasen Shreve replaces #57 Chad Green
t9.pitching_substitution(45)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("b b c")
t9.out("G4-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f f s")
t9.out("K")

# 7. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("c b c s")
t9.out("K")

# Winning team: NYY
# WP: NYY #52 CC Sabathia
game.winning_pitcher(52)

# Loser team: BOS
# LP: BOS #57 Eduardo Rodriguez
game.losing_pitcher(57, is_away_team=True)

# print(game)
game.generate_scorecard()
