import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CWS @ BOS, 2018-06-09
# https://www.baseball-reference.com/boxes/BOS/BOS201806090.shtml
# https://www.mlb.com/gameday/white-sox-vs-red-sox/2018/06/09/530361/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-09 16:05-18:53",
        "at": "Fenway Park, Boston, MA",
        "att": "36,675",
        "temp": "80F, Partly Cloudy",
        "wind": "15mph, Out To RF",
        "away": {
            "team": "Chicago White Sox",
            "starter": 55,
            "roster": {
                # Lineup
                7: "Tim Anderson",
                20: "José Rondón",
                79: "José Abreu",
                24: "Matt Davidson",
                36: "Kevan Smith",
                10: "Yoán Moncada",
                32: "Trayce Thompson",
                18: "Daniel Palka",
                22: "Charles Tilson",
                # Starting pitcher
                55: "Carlos Rodón",
                # Bench
                38: "Omar Narváez",
                5: "Yolmer Sánchez",
                15: "Adam Engel",
                # Bullpen
                65: "Nate Jones",
                52: "Xavier Cedeño",
                48: "Joakim Soria",
                33: "James Shields",
                68: "Dylan Covey",
                40: "Reynaldo López",
                57: "Jace Fry",
                66: "Chris Volstad",
                27: "Lucas Giolito",
                53: "Héctor Santiago",
                70: "Luis Avilán",
                44: "Bruce Rondón",
            },
            "lefties": [55, 52, 57, 53, 70],
            "lineup": [
                [7, "6"],
                [20, "5"],
                [79, "3"],
                [24, "0"],
                [36, "2"],
                [10, "4"],
                [32, "8"],
                [18, "9"],
                [22, "7"],
            ],
            "bench": [
                [38, "C"],
                [5, "3B"],
                [15, "CF"],
            ],
            "bullpen": [65, 52, 48, 33, 68, 40, 57, 66, 27, 53, 70, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
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
                [16, "7"],
                [2, "6"],
                [28, "0"],
                [36, "4"],
                [59, "3"],
                [11, "5"],
                [7, "2"],
                [23, "9"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 44, 22, 41, 61, 37, 46, 76, 65, 56, 32],
        },
        "umpires": {
            "HP": "Shane Livensparger",
            "1B": "James Hoye",
            "2B": "Quinn Wolcott",
            "3B": "Jeff Kellogg",
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

# 1. CWS #7  Tim Anderson (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.hit(1)
t1.advance(2, "20 BB")
t1.advance(4, "79 2B")

# 2. CWS #20 José Rondón (X - X - 7)
t1.new_ab()
t1.pitch_list("c t b 1 b b f b")
t1.reach("BB")
t1.advance(3, "79 2B")
t1.advance(4, "36 G4-3")

# 3. CWS #79 José Abreu (X - 7 - 20)
t1.new_ab()
t1.pitch_list("c")
t1.hit(2, rbis=1)
t1.advance(3, "36 G4-3")

# 4. CWS #24 Matt Davidson (20 - 79 - X)
t1.new_ab()
t1.pitch_list("c c c")
t1.out("!K")

# 5. CWS #36 Kevan Smith (20 - 79 - X)
t1.new_ab()
t1.pitch_list("b f s")
t1.out("G4-3", rbis=1)

# 6. CWS #10 Yoán Moncada (79 - X - X)
t1.new_ab()
t1.pitch_list("c s b c")
t1.out("!K")


# Bot 1st
# Pitching: CWS #55 Carlos Rodón
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b f b f b")
b1.reach("BB")
b1.error(6)
b1.advance(2, "2 E6")
b1.error(4)
b1.advance("U", "28 E4")

# 2. BOS #2  Xander Bogaerts (X - X - 16)
b1.new_ab()
b1.reach("FC6")
b1.thrown_out(2, "28 FC6-4", 1, 55)

# 3. BOS #28 J.D. Martinez (X - 16 - 2)
b1.new_ab()
b1.pitch_list("c b b")
b1.reach("FC6-4")
b1.advance(2, "36 1B")
b1.advance(3, "11 WP")

# 4. BOS #36 Eduardo Núñez (X - X - 28)
b1.new_ab()
b1.pitch_list("t")
b1.hit(1)
b1.advance(2, "11 WP")

# 5. BOS #59 Sam Travis (X - 28 - 36)
b1.new_ab()
b1.pitch_list("c b s s")
b1.out("K")

# 6. BOS #11 Rafael Devers (X - 28 - 36)
b1.new_ab()
b1.pitch_list("f b b")
b1.wp()
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 7. CWS #32 Trayce Thompson (X - X - X)
t2.new_ab()
t2.pitch_list("c c s")
t2.out("K")

# 8. CWS #18 Daniel Palka (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b b")
t2.reach("BB")
t2.thrown_out(2, "22 FC4", 2, 24)

# 9. CWS #22 Charles Tilson (X - X - 18)
t2.new_ab()
t2.pitch_list("c")
t2.reach("FC4")

# 1. CWS #7  Tim Anderson (X - X - 22)
t2.new_ab()
t2.pitch_list("b")
t2.out("F7")


# Bot 2nd
# Pitching: CWS #55 Carlos Rodón
b2 = game.new_inning()

# 7. BOS #7  Christian Vázquez (X - X - X)
b2.new_ab()
b2.out("F9")

# 8. BOS #23 Blake Swihart (X - X - X)
b2.new_ab()
b2.pitch_list("b b f")
b2.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(4, rbis=1)

# 1. BOS #16 Andrew Benintendi (X - X - X)
b2.new_ab()
b2.pitch_list("b s s b b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 2. CWS #20 José Rondón (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("(F)P2")

# 3. CWS #79 José Abreu (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b b")
t3.out("G5-3")

# 4. CWS #24 Matt Davidson (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G5-3")


# Bot 3rd
# Pitching: CWS #55 Carlos Rodón
b3 = game.new_inning()

# 2. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)

# 3. BOS #28 J.D. Martinez (X - X - 2)
b3.new_ab()
b3.pitch_list("b s b f s")
b3.out("K")

# 4. BOS #36 Eduardo Núñez (X - X - 2)
b3.new_ab()
b3.pitch_list("f c s")
b3.out("K")

# 5. BOS #59 Sam Travis (X - X - 2)
b3.new_ab()
b3.pitch_list("1 b f f f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 5. CWS #36 Kevan Smith (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.thrown_out(2, "10 DP6-4-3", 1, 24)

# 6. CWS #10 Yoán Moncada (X - X - 36)
t4.new_ab()
t4.pitch_list("b f f f b 1")
t4.out("DP6-4-3")

# 7. CWS #32 Trayce Thompson (X - X - X)
t4.new_ab()
t4.out("G5-3")


# Bot 4th
# Pitching: CWS #55 Carlos Rodón
b4 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(3, "7 1B")

# 7. BOS #7  Christian Vázquez (X - X - 11)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)

# 8. BOS #23 Blake Swihart (11 - X - 7)
b4.new_ab()
b4.pitch_list("c f d b f b f c")
b4.out("!K")

# 9. BOS #19 Jackie Bradley Jr. (11 - X - 7)
b4.new_ab()
b4.pitch_list("f c s")
b4.out("K")

# 1. BOS #16 Andrew Benintendi (11 - X - 7)
b4.new_ab()
b4.pitch_list("b s s f s")
b4.out("K2-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 8. CWS #18 Daniel Palka (X - X - X)
t5.new_ab()
t5.pitch_list("b b c s c")
t5.out("!K")

# 9. CWS #22 Charles Tilson (X - X - X)
t5.new_ab()
t5.pitch_list("f s b f")
t5.out("L9")

# 1. CWS #7  Tim Anderson (X - X - X)
t5.new_ab()
t5.pitch_list("c s s")
t5.out("K")


# Bot 5th
# Pitching: CWS #55 Carlos Rodón
b5 = game.new_inning()

# 2. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("b c s b")
b5.error(3)
b5.reach("E3")
b5.advance("U", "28 HR")

# 3. BOS #28 J.D. Martinez (X - X - 2)
b5.new_ab()
b5.pitch_list("f")
b5.hit(4, rbis=2)

# 4. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("f s b b f f b f d")
b5.reach("BB")
b5.advance(2, "59 SB")
b5.advance(3, "59 G3-1")
b5.thrown_out(4, "11 FC1", 2, 55)

# 5. BOS #59 Sam Travis (X - X - 36)
b5.new_ab()
b5.pitch_list("c d s f b f")
b5.out("G3-1")

# 6. BOS #11 Rafael Devers (36 - X - X)
b5.new_ab()
b5.pitch_list("b b b")
b5.reach("FC1")

# 7. BOS #7  Christian Vázquez (X - X - 11)
b5.new_ab()
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 2. CWS #20 José Rondón (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.thrown_out(2, "79 DP4-6-3", 1, 24)

# 3. CWS #79 José Abreu (X - X - 20)
t6.new_ab()
t6.pitch_list("b c b s")
t6.out("DP4-6-3")

# 4. CWS #24 Matt Davidson (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c f b")
t6.reach("BB")
t6.advance(3, "36 1B")

# 5. CWS #36 Kevan Smith (X - X - 24)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)

# 6. CWS #10 Yoán Moncada (24 - X - 36)
t6.new_ab()
t6.pitch_list("f b b f s")
t6.out("K")


# Bot 6th
# Pitching: CWS #52 Xavier Cedeño
b6 = game.new_inning()

# Pitching change (CWS): #52 Xavier Cedeño replaces #55 Carlos Rodón
b6.pitching_substitution(52)

# 8. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("b b f f b s")
b6.out("K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b c t b b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #24 David Price
t7.pitching_substitution(56)

# Defensive change (BOS): #12 Brock Holt replaces #23 Blake Swihart (RF), playing RF, batting 8th
t7.defensive_substitution(8, 12, "9")

# 7. CWS #32 Trayce Thompson (X - X - X)
t7.new_ab()
t7.pitch_list("c f f s")
t7.out("K")

# 8. CWS #18 Daniel Palka (X - X - X)
t7.new_ab()
t7.pitch_list("b c c b s")
t7.out("K")

# 9. CWS #22 Charles Tilson (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G1-3")


# Bot 7th
# Pitching: CWS #66 Chris Volstad
b7 = game.new_inning()

# Pitching change (CWS): #66 Chris Volstad replaces #52 Xavier Cedeño
b7.pitching_substitution(66)

# 2. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("b s c b f f b")
b7.out("G6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1)
b7.thrown_out(2, "36 DP4-3", 2, 66)

# 4. BOS #36 Eduardo Núñez (X - X - 28)
b7.new_ab()
b7.pitch_list("c 1 f b")
b7.out("DP4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t8.pitching_substitution(32)

# 1. CWS #7  Tim Anderson (X - X - X)
t8.new_ab()
t8.out("G5-3")

# Offensive change (CWS): Pinch-hitter #5 Yolmer Sánchez replaces #20 José Rondón, batting 2nd
t8.offensive_substitution(2, 5, "PH")

# 2. CWS #5  Yolmer Sánchez (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.hit(3)

# 3. CWS #79 José Abreu (5 - X - X)
t8.new_ab()
t8.pitch_list("c f s")
t8.out("K")

# 4. CWS #24 Matt Davidson (5 - X - X)
t8.new_ab()
t8.pitch_list("b c b d b")
t8.reach("BB")

# 5. CWS #36 Kevan Smith (5 - X - 24)
t8.new_ab()
t8.out("F9")


# Bot 8th
# Pitching: CWS #66 Chris Volstad
b8 = game.new_inning()

# Defensive switch (CWS): #5 Yolmer Sánchez moves to 3B
b8.defensive_switch(5, "5")

# 5. BOS #59 Sam Travis (X - X - X)
b8.new_ab()
b8.pitch_list("b c s f b")
b8.out("G4-3")

# Pitching change (CWS): #70 Luis Avilán replaces #66 Chris Volstad
b8.pitching_substitution(70)

# 6. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("P5")

# 7. BOS #7  Christian Vázquez (X - X - X)
b8.new_ab()
b8.pitch_list("c c")
b8.hit(1)
b8.advance(2, "12 WP")

# 8. BOS #12 Brock Holt (X - X - 7)
b8.new_ab()
b8.pitch_list("b c c b s")
b8.wp()
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t9.pitching_substitution(46)

# Defensive change (BOS): #18 Mitch Moreland replaces #59 Sam Travis (1B), playing 1B, batting 5th
t9.defensive_substitution(5, 18, "3")

# 6. CWS #10 Yoán Moncada (X - X - X)
t9.new_ab()
t9.pitch_list("c c b f b")
t9.out("F7")

# 7. CWS #32 Trayce Thompson (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# 8. CWS #18 Daniel Palka (X - X - X)
t9.new_ab()
t9.pitch_list("b f b s b c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: CWS
# LP: CWS #55 Carlos Rodón
game.losing_pitcher(55, is_away_team=True)

# print(game)
game.generate_scorecard()
