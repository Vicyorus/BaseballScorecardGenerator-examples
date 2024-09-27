import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CWS, 2018-08-30
# https://www.baseball-reference.com/boxes/CHA/CHA201808300.shtml
# https://www.mlb.com/gameday/red-sox-vs-white-sox/2018/08/30/531409/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-30 20:10-23:47",
        "at": "Guaranteed Rate Field, Chicago, IL",
        "att": "18,015",
        "temp": "68F, Partly Cloudy",
        "wind": "10mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                5: "Ian Kinsler",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                25: "Steve Pearce",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [36, "5"],
                [12, "3"],
                [5, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [18, "1B"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Chicago White Sox",
            "starter": 27,
            "roster": {
                # Lineup
                5: "Yolmer Sánchez",
                30: "Nicky Delmonico",
                26: "Avisaíl García",
                18: "Daniel Palka",
                7: "Tim Anderson",
                10: "Yoán Moncada",
                24: "Matt Davidson",
                36: "Kevan Smith",
                15: "Adam Engel",
                # Starting pitcher
                27: "Lucas Giolito",
                # Bench
                20: "José Rondón",
                38: "Omar Narváez",
                25: "Ryan LaMarre",
                # Bullpen
                61: "Ryan Burr",
                50: "Thyago Vieira",
                34: "Michael Kopech",
                55: "Carlos Rodón",
                40: "Reynaldo López",
                33: "James Shields",
                57: "Jace Fry",
                68: "Dylan Covey",
                37: "Juan Minaya",
                54: "Jeanmar Gómez",
                53: "Héctor Santiago",
            },
            "lefties": [55, 57, 53],
            "lineup": [
                [5, "5"],
                [30, "7"],
                [26, "9"],
                [18, "0"],
                [7, "6"],
                [10, "4"],
                [24, "3"],
                [36, "2"],
                [15, "8"],
            ],
            "bench": [
                [20, "SS"],
                [38, "C"],
                [25, "OF"],
            ],
            "bullpen": [61, 50, 34, 55, 40, 33, 57, 68, 37, 54, 53],
        },
        "umpires": {
            "HP": "Ted Barrett",
            "1B": "Will Little",
            "2B": "Lance Barksdale",
            "3B": "Sean Barber",
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
# Pitching: CWS #27 Lucas Giolito
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b c b c b")
t1.reach("BB")
t1.thrown_out(2, "16 POCS", 1, 27)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("b f f 1 1 f 1 b b f c")
t1.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("L6")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. CWS #5  Yolmer Sánchez (X - X - X)
b1.new_ab()
b1.pitch_list("b c f c")
b1.out("!K")

# 2. CWS #30 Nicky Delmonico (X - X - X)
b1.new_ab()
b1.pitch_list("s b b f b b")
b1.reach("BB")
b1.advance(4, "26 HR")

# 3. CWS #26 Avisaíl García (X - X - 30)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(4, rbis=2)

# 4. CWS #18 Daniel Palka (X - X - X)
b1.new_ab()
b1.hit(1)
b1.advance(2, "10 1B")
b1.advance(4, "24 1B")

# 5. CWS #7  Tim Anderson (X - X - 18)
b1.new_ab()
b1.pitch_list("c s s")
b1.out("K")

# 6. CWS #10 Yoán Moncada (X - X - 18)
b1.new_ab()
b1.pitch_list("b f")
b1.hit(1)
b1.advance(3, "24 1B")

# 7. CWS #24 Matt Davidson (X - 18 - 10)
b1.new_ab()
b1.pitch_list("b c f")
b1.hit(1, rbis=1)
b1.thrown_out(2, "36 FC5-4", 3, 22)

# 8. CWS #36 Kevan Smith (10 - X - 24)
b1.new_ab()
b1.reach("FC5-4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CWS #27 Lucas Giolito
t2 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b b c f f s")
t2.out("K")

# 5. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c f f")
t2.out("G4-3")

# 6. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("b b c s f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 9. CWS #15 Adam Engel (X - X - X)
b2.new_ab()
b2.pitch_list("c s s")
b2.out("K")

# 1. CWS #5  Yolmer Sánchez (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(3, "30 2B")
b2.advance(4, "26 SF8")

# 2. CWS #30 Nicky Delmonico (X - X - 5)
b2.new_ab()
b2.pitch_list("b f 1 b b")
b2.hit(2)
b2.advance(3, "26 SF8")

# 3. CWS #26 Avisaíl García (5 - 30 - X)
b2.new_ab()
b2.pitch_list("c b f f")
b2.out("SF8", rbis=1)

# 4. CWS #18 Daniel Palka (30 - X - X)
b2.new_ab()
b2.pitch_list("c c d b d f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CWS #27 Lucas Giolito
t3 = game.new_inning()

# 7. BOS #5  Ian Kinsler (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G5-3")

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("c c b f f f f s")
t3.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c b s b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 5. CWS #7  Tim Anderson (X - X - X)
b3.new_ab()
b3.hit(1)
b3.advance(2, "10 BB")

# 6. CWS #10 Yoán Moncada (X - X - 7)
b3.new_ab()
b3.pitch_list("b b b c s f b")
b3.reach("BB")
b3.thrown_out(2, "36 DP6-4-3", 2, 22)

# 7. CWS #24 Matt Davidson (X - 7 - 10)
b3.new_ab()
b3.pitch_list("c s c")
b3.out("!K")

# 8. CWS #36 Kevan Smith (X - 7 - 10)
b3.new_ab()
b3.out("DP6-4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CWS #27 Lucas Giolito
t4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("c c b")
t4.out("G3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.out("(F)F7")

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("b c b s s")
t4.out("K")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 9. CWS #15 Adam Engel (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b")
b4.out("G6-3")

# 1. CWS #5  Yolmer Sánchez (X - X - X)
b4.new_ab()
b4.pitch_list("s c")
b4.hit(1)

# 2. CWS #30 Nicky Delmonico (X - X - 5)
b4.new_ab()
b4.out("F8")

# 3. CWS #26 Avisaíl García (X - X - 5)
b4.new_ab()
b4.pitch_list("b s b b s c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CWS #27 Lucas Giolito
t5 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("c b s f f f")
t5.error(5)
t5.reach("E5")
t5.advance(2, "36 G5-3")
t5.advance(3, "5 1B")

# 5. BOS #36 Eduardo Núñez (X - X - 2)
t5.new_ab()
t5.pitch_list("s b")
t5.out("G5-3")

# 6. BOS #12 Brock Holt (X - 2 - X)
t5.new_ab()
t5.pitch_list("c c b s")
t5.out("K")

# 7. BOS #5  Ian Kinsler (X - 2 - X)
t5.new_ab()
t5.pitch_list("c f d f f d f")
t5.hit(1)
t5.advance(2, "3 HBP")

# 8. BOS #3  Sandy León (2 - X - 5)
t5.new_ab()
t5.pitch_list("s b s")
t5.reach("HBP")

# 9. BOS #19 Jackie Bradley Jr. (2 - 5 - 3)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G3")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 4. CWS #18 Daniel Palka (X - X - X)
b5.new_ab()
b5.pitch_list("s f b s")
b5.out("K")

# 5. CWS #7  Tim Anderson (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G6-3")

# 6. CWS #10 Yoán Moncada (X - X - X)
b5.new_ab()
b5.pitch_list("b b s f")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CWS #27 Lucas Giolito
t6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b f f")
t6.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t6.new_ab()
t6.pitch_list("f b f c")
t6.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t6.new_ab()
t6.out("F9")

# 4. BOS #2  Xander Bogaerts (X - X - 50)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 7. CWS #24 Matt Davidson (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f f b b b")
b6.reach("BB")
b6.thrown_out(2, "36 DP5-4-3", 1, 44)

# Pitching change (BOS): #44 Brandon Workman replaces #22 Rick Porcello
b6.pitching_substitution(44)

# 8. CWS #36 Kevan Smith (X - X - 24)
b6.new_ab()
b6.pitch_list("c c f 1 b")
b6.out("DP5-4-3")

# 9. CWS #15 Adam Engel (X - X - X)
b6.new_ab()
b6.pitch_list("f s b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CWS #27 Lucas Giolito
t7 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("b b f")
t7.out("(F)P5")

# 6. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("b c b s b b")
t7.reach("BB")
t7.advance(3, "5 1B")
t7.advance(4, "23 1B")

# Pitching change (CWS): #54 Jeanmar Gómez replaces #27 Lucas Giolito
t7.pitching_substitution(54)

# 7. BOS #5  Ian Kinsler (X - X - 12)
t7.new_ab()
t7.pitch_list("1 b")
t7.hit(1)
t7.advance(3, "23 1B")
t7.advance(4, "19 SF8")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #3 Sandy León, batting 8th
t7.offensive_substitution(8, 23, "PH")

# 8. BOS #23 Blake Swihart (12 - X - 5)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(1, rbis=1)
t7.advance(4, "50 HR")

# 9. BOS #19 Jackie Bradley Jr. (5 - X - 23)
t7.new_ab()
t7.pitch_list("b")
t7.out("SF8", rbis=1)

# 1. BOS #50 Mookie Betts (X - X - 23)
t7.new_ab()
t7.pitch_list("1 1 b c")
t7.hit(4, rbis=2)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("b c f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #56 Joe Kelly
b7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #44 Brandon Workman
b7.pitching_substitution(56)

# Defensive switch (BOS): #23 Blake Swihart moves to C
b7.defensive_switch(23, "2")

# 1. CWS #5  Yolmer Sánchez (X - X - X)
b7.new_ab()
b7.hit(1)
b7.advance(2, "26 SB")

# 2. CWS #30 Nicky Delmonico (X - X - 5)
b7.new_ab()
b7.out("F9")

# 3. CWS #26 Avisaíl García (X - X - 5)
b7.new_ab()
b7.pitch_list("s s b b b c")
b7.out("!K")

# 4. CWS #18 Daniel Palka (X - 5 - X)
b7.new_ab()
b7.pitch_list("f c b f f f f d s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CWS #61 Ryan Burr
t8 = game.new_inning()

# Pitching change (CWS): #61 Ryan Burr replaces #54 Jeanmar Gómez
t8.pitching_substitution(61)

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("c s b b f")
t8.out("F9")

# 4. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("b f b f f f b")
t8.out("P4")

# 5. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.out("P4")


# Bot 8th
# Pitching: BOS #70 Ryan Brasier
b8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #56 Joe Kelly
b8.pitching_substitution(70)

# 5. CWS #7  Tim Anderson (X - X - X)
b8.new_ab()
b8.pitch_list("s s f f s")
b8.out("K")

# 6. CWS #10 Yoán Moncada (X - X - X)
b8.new_ab()
b8.pitch_list("f b b")
b8.out("P5")

# 7. CWS #24 Matt Davidson (X - X - X)
b8.new_ab()
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CWS #50 Thyago Vieira
t9 = game.new_inning()

# Pitching change (CWS): #50 Thyago Vieira replaces #61 Ryan Burr
t9.pitching_substitution(50)

# 6. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c b b c c")
t9.out("!K")

# 7. BOS #5  Ian Kinsler (X - X - X)
t9.new_ab()
t9.pitch_list("c f b b b")
t9.hit(1)
t9.advance(2, "23 BB")
t9.advance(4, "19 1B")

# 8. BOS #23 Blake Swihart (X - X - 5)
t9.new_ab()
t9.pitch_list("1 1 1 c 1 b b t b f 1 1 f b")
t9.reach("BB")
t9.advance(3, "19 1B")
t9.advance(4, "16 1B")

# 9. BOS #19 Jackie Bradley Jr. (X - 5 - 23)
t9.new_ab()
t9.pitch_list("c b b f f")
t9.hit(1, rbis=1)
t9.advance(3, "16 1B")
t9.advance(4, "28 HR")

# 1. BOS #50 Mookie Betts (23 - X - 19)
t9.new_ab()
t9.pitch_list("b c c s")
t9.out("K")

# 2. BOS #16 Andrew Benintendi (23 - X - 19)
t9.new_ab()
t9.pitch_list("1 c")
t9.hit(1, rbis=1)
t9.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (19 - X - 16)
t9.new_ab()
t9.pitch_list("b b f")
t9.hit(4, rbis=3)

# 4. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b b")
t9.reach("BB")
t9.advance(2, "36 WP")

# Pitching change (CWS): #53 Héctor Santiago replaces #50 Thyago Vieira
t9.pitching_substitution(53)

# 5. BOS #36 Eduardo Núñez (X - X - 2)
t9.new_ab()
t9.pitch_list("f b f f b b f b")
t9.wp()
t9.reach("BB")
t9.thrown_out(2, "12 FC4-6", 3, 53)

# 6. BOS #12 Brock Holt (X - 2 - 36)
t9.new_ab()
t9.pitch_list("c b b c")
t9.reach("FC4-6")


# Bot 9th
# Pitching: BOS #37 Heath Hembree
b9 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #70 Ryan Brasier
b9.pitching_substitution(37)

# 8. CWS #36 Kevan Smith (X - X - X)
b9.new_ab()
b9.pitch_list("c f f")
b9.out("G4-3")

# 9. CWS #15 Adam Engel (X - X - X)
b9.new_ab()
b9.pitch_list("b c b c")
b9.hit(1)
b9.thrown_out(2, "5 FC1-6", 2, 37)

# 1. CWS #5  Yolmer Sánchez (X - X - 15)
b9.new_ab()
b9.pitch_list("c f b")
b9.reach("FC1-6")
b9.advance(2, "30 DI")

# 2. CWS #30 Nicky Delmonico (X - X - 5)
b9.new_ab()
b9.pitch_list("b c s b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #70 Ryan Brasier
game.winning_pitcher(70, is_away_team=True)

# Loser team: CWS
# LP: CWS #50 Thyago Vieira
game.losing_pitcher(50)

# print(game)
game.generate_scorecard()
