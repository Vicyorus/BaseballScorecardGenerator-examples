import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CWS, 2018-09-01
# https://www.baseball-reference.com/boxes/CHA/CHA201809010.shtml
# https://www.mlb.com/gameday/red-sox-vs-white-sox/2018/09/01/531434/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-01 19:10-22:06",
        "at": "Guaranteed Rate Field, Chicago, IL",
        "att": "22,639",
        "temp": "84F, Partly Cloudy",
        "wind": "9mph, Out To LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                5: "Ian Kinsler",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                30: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                12: "Brock Holt",
                59: "Sam Travis",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
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
            "lefties": [57, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [25, "3"],
                [28, "0"],
                [2, "6"],
                [36, "5"],
                [5, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [18, "1B"],
                [12, "2B"],
                [59, "1B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [47, 35, 44, 67, 22, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Chicago White Sox",
            "starter": 55,
            "roster": {
                # Lineup
                7: "Tim Anderson",
                30: "Nicky Delmonico",
                26: "Avisaíl García",
                24: "Matt Davidson",
                10: "Yoán Moncada",
                25: "Ryan LaMarre",
                38: "Omar Narváez",
                5: "Yolmer Sánchez",
                15: "Adam Engel",
                # Starting pitcher
                55: "Carlos Rodón",
                # Bench
                20: "José Rondón",
                18: "Daniel Palka",
                36: "Kevan Smith",
                # Bullpen
                61: "Ryan Burr",
                33: "James Shields",
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
                [7, "6"],
                [30, "0"],
                [26, "9"],
                [24, "3"],
                [10, "4"],
                [25, "7"],
                [38, "2"],
                [5, "5"],
                [15, "8"],
            ],
            "bench": [
                [20, "SS"],
                [18, "1B"],
                [36, "C"],
            ],
            "bullpen": [61, 33, 67, 68, 37, 54, 50, 34, 63, 39, 40, 57, 27, 53],
        },
        "umpires": {
            "HP": "Lance Barksdale",
            "1B": "Sean Barber",
            "2B": "Ted Barrett",
            "3B": "Will Little",
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
# Pitching: CWS #55 Carlos Rodón
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b b f c")
t1.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F9")

# 3. BOS #25 Steve Pearce (X - X - X)
t1.new_ab()
t1.pitch_list("c s b")
t1.out("G5-3")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. CWS #7  Tim Anderson (X - X - X)
b1.new_ab()
b1.pitch_list("f b b f f s")
b1.out("K")

# 2. CWS #30 Nicky Delmonico (X - X - X)
b1.new_ab()
b1.pitch_list("c f b c")
b1.out("!K")

# 3. CWS #26 Avisaíl García (X - X - X)
b1.new_ab()
b1.pitch_list("b b c s b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CWS #55 Carlos Rodón
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b c f s")
t2.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c s s")
t2.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b b f")
t2.out("F7")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 4. CWS #24 Matt Davidson (X - X - X)
b2.new_ab()
b2.pitch_list("b b s s b s")
b2.out("K")

# 5. CWS #10 Yoán Moncada (X - X - X)
b2.new_ab()
b2.pitch_list("c s b")
b2.out("(F)P3")

# 6. CWS #25 Ryan LaMarre (X - X - X)
b2.new_ab()
b2.pitch_list("b c c b b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CWS #55 Carlos Rodón
t3 = game.new_inning()

# 7. BOS #5  Ian Kinsler (X - X - X)
t3.new_ab()
t3.pitch_list("c s")
t3.out("L8")

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("b b")
t3.out("P3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.hit(3)

# 1. BOS #50 Mookie Betts (19 - X - X)
t3.new_ab()
t3.pitch_list("d c b c f")
t3.out("L7")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 7. CWS #38 Omar Narváez (X - X - X)
b3.new_ab()
b3.pitch_list("c c b c")
b3.out("!K")

# 8. CWS #5  Yolmer Sánchez (X - X - X)
b3.new_ab()
b3.out("F8")

# 9. CWS #15 Adam Engel (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CWS #55 Carlos Rodón
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("F7")

# 3. BOS #25 Steve Pearce (X - X - X)
t4.new_ab()
t4.pitch_list("b s b f f")
t4.reach("HBP")
t4.advance(2, "28 G5-3")

# 4. BOS #28 J.D. Martinez (X - X - 25)
t4.new_ab()
t4.pitch_list("f")
t4.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - 25 - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("(F)P4")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 1. CWS #7  Tim Anderson (X - X - X)
b4.new_ab()
b4.pitch_list("t b f c")
b4.out("!K")

# 2. CWS #30 Nicky Delmonico (X - X - X)
b4.new_ab()
b4.pitch_list("f f b c")
b4.out("!K")

# 3. CWS #26 Avisaíl García (X - X - X)
b4.new_ab()
b4.pitch_list("s c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CWS #55 Carlos Rodón
t5 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("b f b")
t5.hit(4)

# 7. BOS #5  Ian Kinsler (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("G5-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("b c f s")
t5.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.hit(4)

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b c f f f f f")
t5.error(5)
t5.reach("E5")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.out("F8")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 4. CWS #24 Matt Davidson (X - X - X)
b5.new_ab()
b5.pitch_list("b b f")
b5.hit(1)
b5.thrown_out(2, "10 DP4-6-3", 1, 57)

# 5. CWS #10 Yoán Moncada (X - X - 24)
b5.new_ab()
b5.pitch_list("b c f")
b5.out("DP4-6-3")

# 6. CWS #25 Ryan LaMarre (X - X - X)
b5.new_ab()
b5.pitch_list("s b f b b f b")
b5.reach("BB")

# 7. CWS #38 Omar Narváez (X - X - 25)
b5.new_ab()
b5.pitch_list("b b f c f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CWS #55 Carlos Rodón
t6 = game.new_inning()

# 3. BOS #25 Steve Pearce (X - X - X)
t6.new_ab()
t6.pitch_list("f b")
t6.out("G6-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("c s b")
t6.hit(1)
t6.advance(2, "2 BB")
t6.advance(3, "36 G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(2, "36 G4-3")

# 6. BOS #36 Eduardo Núñez (X - 28 - 2)
t6.new_ab()
t6.out("G4-3")

# 7. BOS #5  Ian Kinsler (28 - 2 - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("P4")


# Bot 6th
# Pitching: BOS #57 Eduardo Rodriguez
b6 = game.new_inning()

# 8. CWS #5  Yolmer Sánchez (X - X - X)
b6.new_ab()
b6.pitch_list("b c b f b f")
b6.hit(1)
b6.thrown_out(2, "15 FC4-6", 1, 57)

# 9. CWS #15 Adam Engel (X - X - 5)
b6.new_ab()
b6.pitch_list("s")
b6.reach("FC4-6")
b6.advance(4, "30 2B")

# 1. CWS #7  Tim Anderson (X - X - 15)
b6.new_ab()
b6.pitch_list("f f s")
b6.out("K")

# 2. CWS #30 Nicky Delmonico (X - X - 15)
b6.new_ab()
b6.pitch_list("b f")
b6.hit(2, rbis=1)

# Pitching change (BOS): #70 Ryan Brasier replaces #57 Eduardo Rodriguez
b6.pitching_substitution(70)

# 3. CWS #26 Avisaíl García (X - 30 - X)
b6.new_ab()
b6.pitch_list("c s f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CWS #55 Carlos Rodón
t7 = game.new_inning()

# Defensive change (CWS): #18 Daniel Palka replaces #26 Avisaíl García (RF), playing LF, batting 3rd
t7.defensive_substitution(3, 18, "7")

# Defensive switch (CWS): #25 Ryan LaMarre moves to RF
t7.defensive_switch(25, "9")

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("s f b f b f b b")
t7.reach("BB")
t7.advance(3, "50 2B")
t7.advance(4, "16 E1")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 7)
t7.new_ab()
t7.pitch_list("b t")
t7.out("F7")

# 1. BOS #50 Mookie Betts (X - X - 7)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(2)
t7.advance(3, "16 E1")
t7.advance(4, "25 1B")

# 2. BOS #16 Andrew Benintendi (7 - 50 - X)
t7.new_ab()
t7.pitch_list("f")
t7.error(1)
t7.reach("E1", end_base=2)
t7.advance(3, "25 1B")
t7.advance("U", "28 1B")

# 3. BOS #25 Steve Pearce (50 - 16 - X)
t7.new_ab()
t7.pitch_list("d b c")
t7.hit(1, rbis=1)
t7.advance(2, "28 1B")
t7.thrown_out(3, "2 DP5-3", 2, 61)

# Pitching change (CWS): #61 Ryan Burr replaces #55 Carlos Rodón
t7.pitching_substitution(61)

# 4. BOS #28 J.D. Martinez (16 - X - 25)
t7.new_ab()
t7.pitch_list("1 b")
t7.hit(1, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - 25 - 28)
t7.new_ab()
t7.pitch_list("c")
t7.out("DP5-3")


# Bot 7th
# Pitching: BOS #70 Ryan Brasier
b7 = game.new_inning()

# Defensive change (BOS): #18 Mitch Moreland replaces #25 Steve Pearce (1B), playing 1B, batting 3rd
b7.defensive_substitution(3, 18, "3")

# 4. CWS #24 Matt Davidson (X - X - X)
b7.new_ab()
b7.pitch_list("b f s f b f b")
b7.hit(1)
b7.advance(2, "10 1B")
b7.advance(3, "25 G3-1")

# 5. CWS #10 Yoán Moncada (X - X - 24)
b7.new_ab()
b7.hit(1)
b7.advance(2, "25 G3-1")

# 6. CWS #25 Ryan LaMarre (X - 24 - 10)
b7.new_ab()
b7.pitch_list("b")
b7.out("G3-1")

# 7. CWS #38 Omar Narváez (24 - 10 - X)
b7.new_ab()
b7.pitch_list("c d t s")
b7.out("K")

# 8. CWS #5  Yolmer Sánchez (24 - 10 - X)
b7.new_ab()
b7.pitch_list("c f b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CWS #61 Ryan Burr
t8 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("L8")

# 7. BOS #5  Ian Kinsler (X - X - X)
t8.new_ab()
t8.pitch_list("b b b")
t8.hit(4)

# 8. BOS #7  Christian Vázquez (X - X - X)
t8.new_ab()
t8.pitch_list("c b c")
t8.out("L3")

# Pitching change (CWS): #39 Aaron Bummer replaces #61 Ryan Burr
t8.pitching_substitution(39)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #70 Ryan Brasier
b8.pitching_substitution(32)

# 9. CWS #15 Adam Engel (X - X - X)
b8.new_ab()
b8.pitch_list("s b")
b8.out("(F)F9")

# 1. CWS #7  Tim Anderson (X - X - X)
b8.new_ab()
b8.pitch_list("b b s b f c")
b8.out("!K")

# 2. CWS #30 Nicky Delmonico (X - X - X)
b8.new_ab()
b8.pitch_list("b c b s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CWS #39 Aaron Bummer
t9 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c f")
t9.hit(1)
t9.thrown_out(2, "18 DP6-3", 2, 39)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t9.new_ab()
t9.pitch_list("b b c f t")
t9.out("KT")

# 3. BOS #18 Mitch Moreland (X - X - 50)
t9.new_ab()
t9.pitch_list("b b c s")
t9.out("DP6-3")


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
b9.pitching_substitution(56)

# 3. CWS #18 Daniel Palka (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("F7")

# 4. CWS #24 Matt Davidson (X - X - X)
b9.new_ab()
b9.pitch_list("c b b")
b9.out("F9")

# 5. CWS #10 Yoán Moncada (X - X - X)
b9.new_ab()
b9.pitch_list("b c b f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57, is_away_team=True)

# Loser team: CWS
# LP: CWS #55 Carlos Rodón
game.losing_pitcher(55)

# print(game)
game.generate_scorecard()
