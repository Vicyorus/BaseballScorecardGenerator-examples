import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CWS, 2018-08-31
# https://www.baseball-reference.com/boxes/CHA/CHA201808310.shtml
# https://www.mlb.com/gameday/red-sox-vs-white-sox/2018/08/31/531419/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-31 20:10-01:12 +1 (2:09 delay)",
        "at": "Guaranteed Rate Field, Chicago, IL",
        "att": "23,625",
        "temp": "83F, Partly Cloudy",
        "wind": "9mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                5: "Ian Kinsler",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                25: "Steve Pearce",
                18: "Mitch Moreland",
                12: "Brock Holt",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [36, "5"],
                [23, "3"],
                [5, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [18, "1B"],
                [12, "2B"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Chicago White Sox",
            "starter": 34,
            "roster": {
                # Lineup
                5: "Yolmer Sánchez",
                30: "Nicky Delmonico",
                26: "Avisaíl García",
                18: "Daniel Palka",
                10: "Yoán Moncada",
                24: "Matt Davidson",
                7: "Tim Anderson",
                36: "Kevan Smith",
                15: "Adam Engel",
                # Starting pitcher
                34: "Michael Kopech",
                # Bench
                38: "Omar Narváez",
                20: "José Rondón",
                25: "Ryan LaMarre",
                # Bullpen
                61: "Ryan Burr",
                55: "Carlos Rodón",
                33: "James Shields",
                68: "Dylan Covey",
                37: "Juan Minaya",
                54: "Jeanmar Gómez",
                50: "Thyago Vieira",
                63: "Ian Hamilton",
                40: "Reynaldo López",
                57: "Jace Fry",
                27: "Lucas Giolito",
                53: "Héctor Santiago",
            },
            "lefties": [55, 57, 53],
            "lineup": [
                [5, "5"],
                [30, "7"],
                [26, "9"],
                [18, "0"],
                [10, "4"],
                [24, "3"],
                [7, "6"],
                [36, "2"],
                [15, "8"],
            ],
            "bench": [
                [38, "C"],
                [20, "SS"],
                [25, "OF"],
            ],
            "bullpen": [61, 55, 33, 68, 37, 54, 50, 63, 40, 57, 27, 53],
        },
        "umpires": {
            "HP": "Will Little",
            "1B": "Lance Barksdale",
            "2B": "Sean Barber",
            "3B": "Ted Barrett",
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
# Pitching: CWS #34 Michael Kopech
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.reach("HBP")
t1.advance(2, "16 BB")
t1.thrown_out(3, "28 CS", 1, 34)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
t1.new_ab()
t1.pitch_list("b c b n c")
t1.out("F9")

# 4. BOS #2  Xander Bogaerts (X - X - 16)
t1.new_ab()
t1.pitch_list("b 1")
t1.out("P4")


# Bot 1st
# Pitching: BOS #17 Nathan Eovaldi
b1 = game.new_inning()

# 1. CWS #5  Yolmer Sánchez (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c f")
b1.reach("HBP")
b1.advance(4, "26 2B")

# 2. CWS #30 Nicky Delmonico (X - X - 5)
b1.new_ab()
b1.out("F7")

# 3. CWS #26 Avisaíl García (X - X - 5)
b1.new_ab()
b1.pitch_list("f f")
b1.hit(2, rbis=1)
b1.advance(3, "18 F8")
b1.advance(4, "10 HR")

# 4. CWS #18 Daniel Palka (X - 26 - X)
b1.new_ab()
b1.pitch_list("b f b")
b1.out("F8")

# 5. CWS #10 Yoán Moncada (26 - X - X)
b1.new_ab()
b1.pitch_list("f b f")
b1.hit(4, rbis=2)

# 6. CWS #24 Matt Davidson (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CWS #34 Michael Kopech
t2 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("s")
t2.out("(F)P3")

# 6. BOS #23 Blake Swihart (X - X - X)
t2.new_ab()
t2.pitch_list("c c f f c")
t2.out("!K")

# 7. BOS #5  Ian Kinsler (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(2)

# 8. BOS #3  Sandy León (X - 5 - X)
t2.new_ab()
t2.pitch_list("b f f")
t2.reach("HBP")

# 9. BOS #19 Jackie Bradley Jr. (X - 5 - 3)
t2.new_ab()
t2.out("P4")


# Bot 2nd
# Pitching: BOS #17 Nathan Eovaldi
b2 = game.new_inning()

# 7. CWS #7  Tim Anderson (X - X - X)
b2.new_ab()
b2.out("G4-3")

# 8. CWS #36 Kevan Smith (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(2)

# 9. CWS #15 Adam Engel (X - 36 - X)
b2.new_ab()
b2.pitch_list("c f b")
b2.out("F9")

# 1. CWS #5  Yolmer Sánchez (X - 36 - X)
b2.new_ab()
b2.pitch_list("f b f b")
b2.out("L7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CWS #34 Michael Kopech
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b f")
t3.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.out("(F)P5")

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #17 Nathan Eovaldi
b3 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #17 Nathan Eovaldi
b3.pitching_substitution(31)

# 2. CWS #30 Nicky Delmonico (X - X - X)
b3.new_ab()
b3.pitch_list("b f b f s")
b3.out("K")

# 3. CWS #26 Avisaíl García (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(2)
b3.advance(3, "24 1B")

# 4. CWS #18 Daniel Palka (X - 26 - X)
b3.new_ab()
b3.reach("HBP")
b3.advance(2, "24 1B")

# 5. CWS #10 Yoán Moncada (X - 26 - 18)
b3.new_ab()
b3.pitch_list("c c b b f d s")
b3.out("K")

# 6. CWS #24 Matt Davidson (X - 26 - 18)
b3.new_ab()
b3.hit(1)

# 7. CWS #7  Tim Anderson (26 - 18 - 24)
b3.new_ab()
b3.pitch_list("c s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CWS #68 Dylan Covey
t4 = game.new_inning()

# Pitching change (CWS): #68 Dylan Covey replaces #34 Michael Kopech
t4.pitching_substitution(68)

# 4. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)
t4.advance(2, "36 1B")
t4.advance(3, "23 G4-3")

# 5. BOS #36 Eduardo Núñez (X - X - 2)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.advance(2, "23 G4-3")

# 6. BOS #23 Blake Swihart (X - 2 - 36)
t4.new_ab()
t4.pitch_list("b")
t4.out("G4-3")

# 7. BOS #5  Ian Kinsler (2 - 36 - X)
t4.new_ab()
t4.pitch_list("c c b f f f f b f c")
t4.out("!K")

# 8. BOS #3  Sandy León (2 - 36 - X)
t4.new_ab()
t4.pitch_list("b c b")
t4.out("L8")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# 8. CWS #36 Kevan Smith (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G5-3")

# 9. CWS #15 Adam Engel (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)

# 1. CWS #5  Yolmer Sánchez (X - X - 15)
b4.new_ab()
b4.pitch_list("b c 1 1 b 1 c f f s")
b4.out("K")

# 2. CWS #30 Nicky Delmonico (X - X - 15)
b4.new_ab()
b4.pitch_list("1 f")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CWS #68 Dylan Covey
t5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("b b f f c")
t5.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t5.new_ab()
t5.pitch_list("c f 1 f b b s")
t5.out("K")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# 3. CWS #26 Avisaíl García (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("L6")

# 4. CWS #18 Daniel Palka (X - X - X)
b5.new_ab()
b5.pitch_list("c b t f s")
b5.out("K")

# 5. CWS #10 Yoán Moncada (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(3, "24 1B")

# 6. CWS #24 Matt Davidson (X - X - 10)
b5.new_ab()
b5.pitch_list("d f b")
b5.hit(1)
b5.thrown_out(2, "9-6", 3, 31)


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CWS #68 Dylan Covey
t6 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c f b f b b")
t6.out("G1-3")

# 5. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b c c f f b f b")
t6.out("(F)P3")

# 6. BOS #23 Blake Swihart (X - X - X)
t6.new_ab()
t6.out("G4-3")


# Bot 6th
# Pitching: BOS #31 Drew Pomeranz
b6 = game.new_inning()

# 7. CWS #7  Tim Anderson (X - X - X)
b6.new_ab()
b6.pitch_list("b b s b f f")
b6.out("G5-3")

# 8. CWS #36 Kevan Smith (X - X - X)
b6.new_ab()
b6.pitch_list("b f f")
b6.hit(1)
b6.advance(3, "5 2B")
b6.thrown_out(4, "5 8-4-2", 3, 31)

# 9. CWS #15 Adam Engel (X - X - 36)
b6.new_ab()
b6.pitch_list("b c f f f f d d s")
b6.out("K")

# 1. CWS #5  Yolmer Sánchez (X - X - 36)
b6.new_ab()
b6.pitch_list("c b f")
b6.hit(2)


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CWS #68 Dylan Covey
t7 = game.new_inning()

# 7. BOS #5  Ian Kinsler (X - X - X)
t7.new_ab()
t7.pitch_list("b c c b b b")
t7.reach("BB")
t7.thrown_out(2, "19 CS", 2, 37)

# Pitching change (CWS): #37 Juan Minaya replaces #68 Dylan Covey
t7.pitching_substitution(37)

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #3 Sandy León, batting 8th
t7.offensive_substitution(8, 18, "PH")

# 8. BOS #18 Mitch Moreland (X - X - 5)
t7.new_ab()
t7.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 5)
t7.new_ab()
t7.pitch_list("1 b b")
t7.out("F7")


# Bot 7th
# Pitching: BOS #47 Tyler Thornburg
b7 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #31 Drew Pomeranz
b7.pitching_substitution(47)

# Defensive switch (BOS): #23 Blake Swihart moves to C
b7.defensive_switch(23, "2")

# Defensive switch (BOS): #18 Mitch Moreland moves to 1B
b7.defensive_switch(18, "3")

# 2. CWS #30 Nicky Delmonico (X - X - X)
b7.new_ab()
b7.pitch_list("s c s")
b7.out("K")

# 3. CWS #26 Avisaíl García (X - X - X)
b7.new_ab()
b7.pitch_list("c b b f b b")
b7.reach("BB")
b7.advance(2, "18 1B")
b7.advance(4, "24 HR")

# 4. CWS #18 Daniel Palka (X - X - 26)
b7.new_ab()
b7.pitch_list("f")
b7.hit(1)
b7.advance(4, "24 HR")

# 5. CWS #10 Yoán Moncada (X - 26 - 18)
b7.new_ab()
b7.pitch_list("s d b b c s")
b7.out("K")

# 6. CWS #24 Matt Davidson (X - 26 - 18)
b7.new_ab()
b7.pitch_list("b f c d")
b7.hit(4, rbis=3)

# 7. CWS #7  Tim Anderson (X - X - X)
b7.new_ab()
b7.pitch_list("b b s b")
b7.hit(1)
b7.advance(2, "36 BB")

# 8. CWS #36 Kevan Smith (X - X - 7)
b7.new_ab()
b7.pitch_list("c b b f d b")
b7.reach("BB")

# 9. CWS #15 Adam Engel (X - 7 - 36)
b7.new_ab()
b7.pitch_list("f f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CWS #37 Juan Minaya
t8 = game.new_inning()

# Defensive change (CWS): #25 Ryan LaMarre replaces #30 Nicky Delmonico (LF), playing LF, batting 2nd
t8.defensive_substitution(2, 25, "7")

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b")
t8.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c")
t8.hit(4)

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("s c s")
t8.out("K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c c c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #44 Brandon Workman
b8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #47 Tyler Thornburg
b8.pitching_substitution(44)

# Defensive change (BOS): #12 Brock Holt replaces #2 Xander Bogaerts (SS), playing SS, batting 4th
b8.defensive_substitution(4, 12, "6")

# 1. CWS #5  Yolmer Sánchez (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.out("F9")

# 2. CWS #25 Ryan LaMarre (X - X - X)
b8.new_ab()
b8.pitch_list("b f f s")
b8.out("K")

# 3. CWS #26 Avisaíl García (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.hit(1)

# 4. CWS #18 Daniel Palka (X - X - 26)
b8.new_ab()
b8.pitch_list("b f b s")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CWS #63 Ian Hamilton
t9 = game.new_inning()

# Pitching change (CWS): #63 Ian Hamilton replaces #37 Juan Minaya
t9.pitching_substitution(63)

# 5. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.out("G4-3")

# 6. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("L5")

# 7. BOS #5  Ian Kinsler (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.out("L9")

# Winning team: CWS
# WP: CWS #68 Dylan Covey
game.winning_pitcher(68)

# Loser team: BOS
# LP: BOS #17 Nathan Eovaldi
game.losing_pitcher(17, is_away_team=True)

# print(game)
game.generate_scorecard()
