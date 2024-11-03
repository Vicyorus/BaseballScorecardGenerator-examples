import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CWS, 2018-09-02
# https://www.baseball-reference.com/boxes/CHA/CHA201809020.shtml
# https://www.mlb.com/gameday/red-sox-vs-white-sox/2018/09/02/531449/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-02 14:42-17:54",
        "at": "Guaranteed Rate Field, Chicago, IL",
        "att": "30,745",
        "temp": "87F, Partly Cloudy",
        "wind": "14mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                36: "Eduardo Núñez",
                5: "Ian Kinsler",
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                59: "Sam Travis",
                16: "Andrew Benintendi",
                3: "Sandy León",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [61, 57, 31, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [2, "6"],
                [18, "3"],
                [28, "7"],
                [36, "5"],
                [5, "4"],
                [12, "0"],
                [23, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [59, "1B"],
                [16, "LF"],
                [3, "C"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 31, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Chicago White Sox",
            "starter": 33,
            "roster": {
                # Lineup
                25: "Ryan LaMarre",
                7: "Tim Anderson",
                24: "Matt Davidson",
                18: "Daniel Palka",
                20: "José Rondón",
                36: "Kevan Smith",
                10: "Yoán Moncada",
                5: "Yolmer Sánchez",
                15: "Adam Engel",
                # Starting pitcher
                33: "James Shields",
                # Bench
                38: "Omar Narváez",
                26: "Avisaíl García",
                30: "Nicky Delmonico",
                21: "Welington Castillo",
                # Bullpen
                61: "Ryan Burr",
                55: "Carlos Rodón",
                67: "Caleb Frare",
                68: "Dylan Covey",
                37: "Juan Minaya",
                54: "Jeanmar Gómez",
                50: "Thyago Vieira",
                34: "Michael Kopech",
                63: "Ian Hamilton",
                39: "Aaron Bummer",
                40: "Reynaldo López",
                57: "Jace Fry",
                27: "Lucas Giolito",
                53: "Héctor Santiago",
            },
            "lefties": [55, 67, 39, 57, 53],
            "lineup": [
                [25, "9"],
                [7, "6"],
                [24, "3"],
                [18, "7"],
                [20, "0"],
                [36, "2"],
                [10, "4"],
                [5, "5"],
                [15, "8"],
            ],
            "bench": [
                [38, "C"],
                [26, "RF"],
                [30, "LF"],
                [21, "C"],
            ],
            "bullpen": [61, 55, 67, 68, 37, 54, 50, 34, 63, 39, 40, 57, 27, 53],
        },
        "umpires": {
            "HP": "Sean Barber",
            "1B": "Ted Barrett",
            "2B": "Will Little",
            "3B": "Lance Barksdale",
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
# Pitching: CWS #33 James Shields
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F9")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("c b c")
t1.hit(1)
t1.advance(2, "28 WP")

# 3. BOS #18 Mitch Moreland (X - X - 2)
t1.new_ab()
t1.pitch_list("c c")
t1.out("F7")

# 4. BOS #28 J.D. Martinez (X - X - 2)
t1.new_ab(is_risp=True)
t1.pitch_list("s b d b s b")
t1.wp()
t1.reach("BB")

# 5. BOS #36 Eduardo Núñez (X - 2 - 28)
t1.new_ab(is_risp=True)
t1.pitch_list("d")
t1.out("L8")


# Bot 1st
# Pitching: BOS #61 Brian Johnson
b1 = game.new_inning()

# 1. CWS #25 Ryan LaMarre (X - X - X)
b1.new_ab()
b1.pitch_list("c c b s")
b1.out("K")

# 2. CWS #7  Tim Anderson (X - X - X)
b1.new_ab()
b1.hit(4)

# 3. CWS #24 Matt Davidson (X - X - X)
b1.new_ab()
b1.pitch_list("c s b f")
b1.hit(1)
b1.advance(2, "20 BB")
b1.advance(4, "36 1B")

# 4. CWS #18 Daniel Palka (X - X - 24)
b1.new_ab()
b1.pitch_list("c f f s")
b1.out("K")

# 5. CWS #20 José Rondón (X - X - 24)
b1.new_ab()
b1.pitch_list("c b b s b b")
b1.reach("BB")
b1.advance(2, "36 1B")
b1.advance(3, "10 1B")

# 6. CWS #36 Kevan Smith (X - 24 - 20)
b1.new_ab(is_risp=True)
b1.pitch_list("c f f")
b1.hit(1, rbis=1)
b1.advance(2, "10 1B")

# 7. CWS #10 Yoán Moncada (X - 20 - 36)
b1.new_ab(is_risp=True)
b1.hit(1)

# 8. CWS #5  Yolmer Sánchez (20 - 36 - 10)
b1.new_ab(is_risp=True)
b1.pitch_list("s")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CWS #33 James Shields
t2 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b f c")
t2.out("!K")

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("b b c f c")
t2.out("!K")

# 8. BOS #23 Blake Swihart (X - X - X)
t2.new_ab()
t2.pitch_list("b s")
t2.hit(1)
t2.advance(2, "19 SB")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 23)
t2.new_ab(is_risp=True)
t2.pitch_list("d b f s d f f f")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #61 Brian Johnson
b2 = game.new_inning()

# 9. CWS #15 Adam Engel (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(2, "25 1B")
b2.advance(3, "7 F7")
b2.advance(4, "24 2B")

# 1. CWS #25 Ryan LaMarre (X - X - 15)
b2.new_ab()
b2.pitch_list("f")
b2.hit(1)
b2.advance(4, "24 2B")

# 2. CWS #7  Tim Anderson (X - 15 - 25)
b2.new_ab(is_risp=True)
b2.pitch_list("b d c d")
b2.out("F7")

# 3. CWS #24 Matt Davidson (15 - X - 25)
b2.new_ab(is_risp=True)
b2.pitch_list("d")
b2.hit(2, rbis=2)

# Pitching change (BOS): #66 Bobby Poyner replaces #61 Brian Johnson
b2.pitching_substitution(66)

# 4. CWS #18 Daniel Palka (X - 24 - X)
b2.new_ab(is_risp=True)
b2.out("F9")

# 5. CWS #20 José Rondón (X - 24 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b b c")
b2.out("P4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CWS #33 James Shields
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c s s")
t3.out("K")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("f b")
t3.out("L7")

# 3. BOS #18 Mitch Moreland (X - X - X)
t3.new_ab()
t3.pitch_list("b s f b b b")
t3.reach("BB")

# 4. BOS #28 J.D. Martinez (X - X - 18)
t3.new_ab()
t3.pitch_list("s b")
t3.out("L8")


# Bot 3rd
# Pitching: BOS #66 Bobby Poyner
b3 = game.new_inning()

# 6. CWS #36 Kevan Smith (X - X - X)
b3.new_ab()
b3.pitch_list("b b f b f b")
b3.reach("BB")
b3.thrown_out(2, "5 FC6-4", 2, 66)

# 7. CWS #10 Yoán Moncada (X - X - 36)
b3.new_ab()
b3.pitch_list("b s f b b s")
b3.out("K")

# 8. CWS #5  Yolmer Sánchez (X - X - 36)
b3.new_ab()
b3.pitch_list("b")
b3.reach("FC6-4")
b3.advance(2, "15 SB")
b3.advance(4, "15 1B")

# 9. CWS #15 Adam Engel (X - X - 5)
b3.new_ab(is_risp=True)
b3.pitch_list("1 b c 1 b f b f f")
b3.hit(1, rbis=1)
b3.advance(2, "25 SB")

# 1. CWS #25 Ryan LaMarre (X - X - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("s f b b")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CWS #33 James Shields
t4 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("c b f f f b b f f f")
t4.out("G6-3")

# 6. BOS #5  Ian Kinsler (X - X - X)
t4.new_ab()
t4.pitch_list("f s b t")
t4.out("KT")

# 7. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.reach("HBP")

# 8. BOS #23 Blake Swihart (X - X - 12)
t4.new_ab()
t4.pitch_list("b")
t4.out("F9")


# Bot 4th
# Pitching: BOS #67 William Cuevas
b4 = game.new_inning()

# Pitching change (BOS): #67 William Cuevas replaces #66 Bobby Poyner
b4.pitching_substitution(67)

# 2. CWS #7  Tim Anderson (X - X - X)
b4.new_ab()
b4.pitch_list("c f s")
b4.out("K")

# 3. CWS #24 Matt Davidson (X - X - X)
b4.new_ab()
b4.pitch_list("b c f s")
b4.out("K")

# 4. CWS #18 Daniel Palka (X - X - X)
b4.new_ab()
b4.pitch_list("b f f b b")
b4.hit(4)

# 5. CWS #20 José Rondón (X - X - X)
b4.new_ab()
b4.pitch_list("b f c b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CWS #33 James Shields
t5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("f b b c s")
t5.out("K2-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G4-3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "18 SB")

# 3. BOS #18 Mitch Moreland (X - X - 2)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c b s s")
t5.out("K")


# Bot 5th
# Pitching: BOS #67 William Cuevas
b5 = game.new_inning()

# 6. CWS #36 Kevan Smith (X - X - X)
b5.new_ab()
b5.pitch_list("b b t b b")
b5.reach("BB")
b5.advance(3, "5 1B")

# 7. CWS #10 Yoán Moncada (X - X - 36)
b5.new_ab()
b5.pitch_list("b s b s b s")
b5.out("K")

# 8. CWS #5  Yolmer Sánchez (X - X - 36)
b5.new_ab()
b5.pitch_list("s b b")
b5.hit(1)

# 9. CWS #15 Adam Engel (36 - X - 5)
b5.new_ab(is_risp=True)
b5.pitch_list("s s s")
b5.out("K")

# 1. CWS #25 Ryan LaMarre (36 - X - 5)
b5.new_ab(is_risp=True)
b5.pitch_list("c b b f f")
b5.out("G3-1")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CWS #33 James Shields
t6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.thrown_out(2, "36 DP6-3", 1, 33)

# 5. BOS #36 Eduardo Núñez (X - X - 28)
t6.new_ab()
t6.out("DP6-3")

# 6. BOS #5  Ian Kinsler (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("P4")


# Bot 6th
# Pitching: BOS #67 William Cuevas
b6 = game.new_inning()

# 2. CWS #7  Tim Anderson (X - X - X)
b6.new_ab()
b6.pitch_list("s b")
b6.hit(2)
b6.advance(3, "18 F9")
b6.advance(4, "20 FC1-6")

# 3. CWS #24 Matt Davidson (X - 7 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.reach("HBP")
b6.thrown_out(2, "20 FC1-6", 2, 67)

# 4. CWS #18 Daniel Palka (X - 7 - 24)
b6.new_ab(is_risp=True)
b6.pitch_list("s")
b6.out("F9")

# 5. CWS #20 José Rondón (7 - X - 24)
b6.new_ab(is_risp=True)
b6.pitch_list("d f c")
b6.reach("FC1-6", rbis=1)
b6.advance(2, "36 WP")
b6.advance(3, "10 1B")

# Pitching change (BOS): #63 Robby Scott replaces #67 William Cuevas
b6.pitching_substitution(63)

# 6. CWS #36 Kevan Smith (X - X - 20)
b6.new_ab(is_risp=True)
b6.pitch_list("d b b b")
b6.wp()
b6.reach("BB")
b6.advance(2, "10 1B")

# 7. CWS #10 Yoán Moncada (X - 20 - 36)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.hit(1)

# 8. CWS #5  Yolmer Sánchez (20 - 36 - 10)
b6.new_ab(is_risp=True)
b6.pitch_list("b b c b")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CWS #67 Caleb Frare
t7 = game.new_inning()

# Pitching change (CWS): #67 Caleb Frare replaces #33 James Shields
t7.pitching_substitution(67)

# Defensive change (CWS): #30 Nicky Delmonico replaces #25 Ryan LaMarre (RF), playing LF, batting 1st
t7.defensive_substitution(1, 30, "7")

# Defensive switch (CWS): #18 Daniel Palka moves to RF
t7.defensive_switch(18, "9")

# 7. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G4-3")

# 8. BOS #23 Blake Swihart (X - X - X)
t7.new_ab()
t7.pitch_list("c f f s")
t7.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("s c b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #63 Robby Scott
b7 = game.new_inning()

# Pitching change (BOS): #63 Robby Scott replaces #63 Robby Scott, batting 6th
b7.pitching_substitution(63)
b7.defensive_substitution(6, 63, "1")

# Defensive change (BOS): #59 Sam Travis replaces #2 Xander Bogaerts (SS), playing RF, batting 2nd
b7.defensive_substitution(2, 59, "9")

# Defensive change (BOS): #30 Tzu-Wei Lin replaces #50 Mookie Betts (RF), playing SS, batting 1st
b7.defensive_substitution(1, 30, "6")

# Defensive change (BOS): #25 Steve Pearce replaces #18 Mitch Moreland (1B), playing 1B, batting 3rd
b7.defensive_substitution(3, 25, "3")

# Defensive change (BOS): #3 Sandy León replaces #36 Eduardo Núñez (3B), playing C, batting 5th
b7.defensive_substitution(5, 3, "2")

# Defensive switch (BOS): #12 Brock Holt moves to 2B
b7.defensive_switch(12, "4")

# Defensive switch (BOS): #23 Blake Swihart moves to 3B
b7.defensive_switch(23, "5")

# 9. CWS #15 Adam Engel (X - X - X)
b7.new_ab()
b7.pitch_list("b s f f f b b s")
b7.out("K")

# 1. CWS #30 Nicky Delmonico (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.reach("HBP")
b7.advance(3, "7 2B")

# 2. CWS #7  Tim Anderson (X - X - 30)
b7.new_ab()
b7.pitch_list("d")
b7.hit(2)

# 3. CWS #24 Matt Davidson (30 - 7 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b s b b s c")
b7.out("!K")

# 4. CWS #18 Daniel Palka (30 - 7 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c c s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CWS #37 Juan Minaya
t8 = game.new_inning()

# Pitching change (CWS): #37 Juan Minaya replaces #67 Caleb Frare
t8.pitching_substitution(37)

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
t8.new_ab()
t8.pitch_list("c f f b s")
t8.out("K")

# 2. BOS #59 Sam Travis (X - X - X)
t8.new_ab()
t8.pitch_list("c b f f c")
t8.out("!K")

# 3. BOS #25 Steve Pearce (X - X - X)
t8.new_ab()
t8.pitch_list("f b b")
t8.out("F9")


# Bot 8th
# Pitching: BOS #76 Hector Velázquez
b8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #63 Robby Scott, batting 6th
b8.pitching_substitution(76)
b8.defensive_substitution(6, 76, "1")

# 5. CWS #20 José Rondón (X - X - X)
b8.new_ab()
b8.pitch_list("b t")
b8.hit(1)
b8.advance(2, "10 G1-3")
b8.advance(3, "5 PB")
b8.advance(4, "5 1B")

# 6. CWS #36 Kevan Smith (X - X - 20)
b8.new_ab()
b8.pitch_list("b c f d b")
b8.out("L8")

# 7. CWS #10 Yoán Moncada (X - X - 20)
b8.new_ab()
b8.pitch_list("c")
b8.out("G1-3")

# 8. CWS #5  Yolmer Sánchez (X - 20 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c c b f d")
b8.pb()
b8.hit(1, rbis=1)

# 9. CWS #15 Adam Engel (X - X - 5)
b8.new_ab()
b8.pitch_list("b f s b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CWS #53 Héctor Santiago
t9 = game.new_inning()

# Pitching change (CWS): #53 Héctor Santiago replaces #37 Juan Minaya
t9.pitching_substitution(53)

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(2, "12 DI")

# 5. BOS #3  Sandy León (X - X - 28)
t9.new_ab()
t9.pitch_list("b c f t")
t9.out("KT")

# Offensive change (BOS): Pinch-hitter #7 Christian Vázquez replaces #76 Hector Velázquez, batting 6th
t9.offensive_substitution(6, 7, "PH")

# 6. BOS #7  Christian Vázquez (X - X - 28)
t9.new_ab()
t9.pitch_list("f f b b s")
t9.out("K")

# 7. BOS #12 Brock Holt (X - X - 28)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b c f b f b")
t9.reach("BB")

# 8. BOS #23 Blake Swihart (X - 28 - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.out("(F)P2")

# Winning team: CWS
# WP: CWS #33 James Shields
game.winning_pitcher(33)

# Loser team: BOS
# LP: BOS #61 Brian Johnson
game.losing_pitcher(61, is_away_team=True)

# print(game)
game.generate_scorecard()
