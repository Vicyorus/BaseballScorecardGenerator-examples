import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIN @ BOS, 2018-07-29
# https://www.baseball-reference.com/boxes/BOS/BOS201807290.shtml
# https://www.mlb.com/gameday/twins-vs-red-sox/2018/07/29/530992/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-29 13:07-15:49",
        "at": "Fenway Park, Boston, MA",
        "att": "36,785",
        "temp": "83F, Partly Cloudy",
        "wind": "7mph, Out To RF",
        "away": {
            "team": "Minnesota Twins",
            "starter": 17,
            "roster": {
                # Lineup
                7: "Joe Mauer",
                20: "Eddie Rosario",
                11: "Jorge Polanco",
                2: "Brian Dozier",
                99: "Logan Morrison",
                22: "Miguel Sanó",
                36: "Robbie Grossman",
                60: "Jake Cave",
                46: "Bobby Wilson",
                # Starting pitcher
                17: "José Berríos",
                # Bench
                23: "Mitch Garver",
                16: "Ehire Adrianza",
                26: "Max Kepler",
                # Bullpen
                12: "Jake Odorizzi",
                54: "Ervin Santana",
                38: "Matt Belisle",
                58: "Gabriel Moya",
                56: "Fernando Rodney",
                55: "Taylor Rogers",
                49: "Adalberto Mejía",
                68: "Matt Magill",
                44: "Kyle Gibson",
                39: "Trevor Hildenberger",
            },
            "lefties": [58, 55, 49],
            "lineup": [
                [7, "0"],
                [20, "7"],
                [11, "6"],
                [2, "4"],
                [99, "3"],
                [22, "5"],
                [36, "9"],
                [60, "8"],
                [46, "2"],
            ],
            "bench": [
                [23, "DH"],
                [16, "3B"],
                [26, "RF"],
            ],
            "bullpen": [12, 54, 38, 58, 56, 55, 49, 68, 44, 39],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                25: "Steve Pearce",
                19: "Jackie Bradley Jr.",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                12: "Brock Holt",
                3: "Sandy León",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                # Bullpen
                47: "Tyler Thornburg",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                22: "Rick Porcello",
                56: "Joe Kelly",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [24, 31, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [25, "3"],
                [19, "8"],
                [36, "4"],
                [23, "5"],
                [12, "6"],
                [3, "2"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [2, "2B"],
            ],
            "bullpen": [47, 24, 46, 76, 70, 22, 56, 31, 61, 32, 37],
        },
        "umpires": {
            "HP": "Doug Eddings",
            "1B": "Marty Foster",
            "2B": "Joe West",
            "3B": "Mark Ripperger",
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
# Pitching: BOS #17 Nathan Eovaldi
t1 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
t1.new_ab()
t1.pitch_list("c f f f b")
t1.out("G4-3")

# 2. MIN #20 Eddie Rosario (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(2)

# 3. MIN #11 Jorge Polanco (X - 20 - X)
t1.new_ab()
t1.pitch_list("c b f b f")
t1.out("F8")

# 4. MIN #2  Brian Dozier (X - 20 - X)
t1.new_ab()
t1.pitch_list("b b b c f s")
t1.out("K")


# Bot 1st
# Pitching: MIN #17 José Berríos
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("(F)P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c f b")
b1.hit(1)
b1.advance(2, "28 BB")
b1.error(6)
b1.advance(3, "25 E6")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b1.new_ab()
b1.pitch_list("c b 1 1 b b b")
b1.reach("BB")
b1.advance(2, "25 E6")

# 4. BOS #25 Steve Pearce (X - 16 - 28)
b1.new_ab()
b1.pitch_list("c b b")
b1.reach("FC6")

# 5. BOS #19 Jackie Bradley Jr. (16 - 28 - 25)
b1.new_ab()
b1.pitch_list("b f b s b s")
b1.out("K")

# 6. BOS #36 Eduardo Núñez (16 - 28 - 25)
b1.new_ab()
b1.pitch_list("s f d")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #17 Nathan Eovaldi
t2 = game.new_inning()

# 5. MIN #99 Logan Morrison (X - X - X)
t2.new_ab()
t2.pitch_list("c b c s")
t2.out("K")

# 6. MIN #22 Miguel Sanó (X - X - X)
t2.new_ab()
t2.pitch_list("f f b s")
t2.out("K")

# 7. MIN #36 Robbie Grossman (X - X - X)
t2.new_ab()
t2.pitch_list("c c")
t2.hit(1)

# 8. MIN #60 Jake Cave (X - X - 36)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")


# Bot 2nd
# Pitching: MIN #17 José Berríos
b2 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
b2.new_ab()
b2.pitch_list("c b c")
b2.hit(1)
b2.advance(2, "12 HBP")
b2.thrown_out(3, "3 FC1-5", 1, 17)

# 8. BOS #12 Brock Holt (X - X - 23)
b2.new_ab()
b2.pitch_list("1")
b2.reach("HBP")
b2.advance(2, "3 FC1-5")
b2.advance(3, "50 FC6-4")
b2.advance(4, "28 2B")

# 9. BOS #3  Sandy León (X - 23 - 12)
b2.new_ab()
b2.pitch_list("b b")
b2.reach("FC1-5")
b2.thrown_out(2, "50 FC6-4", 2, 17)

# 1. BOS #50 Mookie Betts (X - 12 - 3)
b2.new_ab()
b2.pitch_list("c f d")
b2.reach("FC6-4")
b2.advance(2, "16 BB")
b2.advance(4, "28 2B")

# 2. BOS #16 Andrew Benintendi (12 - X - 50)
b2.new_ab()
b2.pitch_list("b d f d b")
b2.reach("BB")
b2.advance(3, "28 2B")

# 3. BOS #28 J.D. Martinez (12 - 50 - 16)
b2.new_ab()
b2.pitch_list("s d b b")
b2.hit(2, rbis=2)

# 4. BOS #25 Steve Pearce (16 - 28 - X)
b2.new_ab()
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #17 Nathan Eovaldi
t3 = game.new_inning()

# 9. MIN #46 Bobby Wilson (X - X - X)
t3.new_ab()
t3.pitch_list("c b f f")
t3.out("L8")

# 1. MIN #7  Joe Mauer (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")

# 2. MIN #20 Eddie Rosario (X - X - X)
t3.new_ab()
t3.out("G4-3")


# Bot 3rd
# Pitching: MIN #17 José Berríos
b3 = game.new_inning()

# 5. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c b b f c")
b3.out("!K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(3, "23 2B")

# 7. BOS #23 Blake Swihart (X - X - 36)
b3.new_ab()
b3.pitch_list("b")
b3.hit(2)

# 8. BOS #12 Brock Holt (36 - 23 - X)
b3.new_ab()
b3.pitch_list("b f c c")
b3.out("!K")

# 9. BOS #3  Sandy León (36 - 23 - X)
b3.new_ab()
b3.pitch_list("c c")
b3.out("G3-1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #17 Nathan Eovaldi
t4 = game.new_inning()

# 3. MIN #11 Jorge Polanco (X - X - X)
t4.new_ab()
t4.pitch_list("c s")
t4.hit(1)
t4.thrown_out(2, "2 DP5-4-3", 1, 17)

# 4. MIN #2  Brian Dozier (X - X - 11)
t4.new_ab()
t4.pitch_list("b c")
t4.out("DP5-4-3")

# 5. MIN #99 Logan Morrison (X - X - X)
t4.new_ab()
t4.pitch_list("b s")
t4.out("F7")


# Bot 4th
# Pitching: MIN #17 José Berríos
b4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f b")
b4.out("L7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(2)
b4.advance(4, "28 1B")

# 3. BOS #28 J.D. Martinez (X - 16 - X)
b4.new_ab()
b4.pitch_list("c f b d b")
b4.hit(1, rbis=1)
b4.advance(2, "19 1B")
b4.advance(3, "36 BB")

# 4. BOS #25 Steve Pearce (X - X - 28)
b4.new_ab()
b4.pitch_list("b f f b s")
b4.out("K")

# 5. BOS #19 Jackie Bradley Jr. (X - X - 28)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(1)
b4.advance(2, "36 BB")

# 6. BOS #36 Eduardo Núñez (X - 28 - 19)
b4.new_ab()
b4.pitch_list("d d b b")
b4.reach("BB")

# 7. BOS #23 Blake Swihart (28 - 19 - 36)
b4.new_ab()
b4.pitch_list("c f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #17 Nathan Eovaldi
t5 = game.new_inning()

# 6. MIN #22 Miguel Sanó (X - X - X)
t5.new_ab()
t5.pitch_list("b c b b")
t5.out("F8")

# 7. MIN #36 Robbie Grossman (X - X - X)
t5.new_ab()
t5.out("G3-1")

# 8. MIN #60 Jake Cave (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)

# 9. MIN #46 Bobby Wilson (X - X - 60)
t5.new_ab()
t5.out("F9")


# Bot 5th
# Pitching: MIN #17 José Berríos
b5 = game.new_inning()

# 8. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("f c b")
b5.out("F8")

# 9. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("s s b c")
b5.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b")
b5.hit(1)

# Pitching change (MIN): #58 Gabriel Moya replaces #17 José Berríos
b5.pitching_substitution(58)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b5.new_ab()
b5.out("P4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #17 Nathan Eovaldi
t6 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
t6.new_ab()
t6.pitch_list("c c")
t6.out("L5")

# 2. MIN #20 Eddie Rosario (X - X - X)
t6.new_ab()
t6.pitch_list("f b f s")
t6.out("K")

# 3. MIN #11 Jorge Polanco (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.out("F7")


# Bot 6th
# Pitching: MIN #49 Adalberto Mejía
b6 = game.new_inning()

# Pitching change (MIN): #49 Adalberto Mejía replaces #58 Gabriel Moya
b6.pitching_substitution(49)

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.out("L9")

# 4. BOS #25 Steve Pearce (X - X - X)
b6.new_ab()
b6.pitch_list("c s b s")
b6.out("K")

# 5. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #17 Nathan Eovaldi
t7 = game.new_inning()

# 4. MIN #2  Brian Dozier (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f f")
t7.out("(F)P2")

# 5. MIN #99 Logan Morrison (X - X - X)
t7.new_ab()
t7.pitch_list("s f b f")
t7.out("F9")

# 6. MIN #22 Miguel Sanó (X - X - X)
t7.new_ab()
t7.pitch_list("f f c")
t7.out("!K")


# Bot 7th
# Pitching: MIN #49 Adalberto Mejía
b7 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.hit(1)

# 7. BOS #23 Blake Swihart (X - X - 36)
b7.new_ab()
b7.pitch_list("1 b f f b")
b7.out("P4")

# 8. BOS #12 Brock Holt (X - X - 36)
b7.new_ab()
b7.pitch_list("l b b 1 b s s")
b7.out("K")

# 9. BOS #3  Sandy León (X - X - 36)
b7.new_ab()
b7.pitch_list("f b c b b f f")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #17 Nathan Eovaldi
t8.pitching_substitution(32)

# Defensive switch (BOS): #36 Eduardo Núñez moves to 3B
t8.defensive_switch(36, "5")

# Defensive change (BOS): #5 Tzu-Wei Lin replaces #23 Blake Swihart (3B), playing SS, batting 7th
t8.defensive_substitution(7, 5, "6")

# Defensive switch (BOS): #12 Brock Holt moves to 2B
t8.defensive_switch(12, "4")

# 7. MIN #36 Robbie Grossman (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b b")
t8.reach("BB")
t8.thrown_out(2, "7 FC6", 3, 32)

# 8. MIN #60 Jake Cave (X - X - 36)
t8.new_ab()
t8.pitch_list("b c s s")
t8.out("K")

# Offensive change (MIN): Pinch-hitter #26 Max Kepler replaces #46 Bobby Wilson, batting 9th
t8.offensive_substitution(9, 26, "PH")

# 9. MIN #26 Max Kepler (X - X - 36)
t8.new_ab()
t8.pitch_list("1 1 c d s b c")
t8.out("!K")

# 1. MIN #7  Joe Mauer (X - X - 36)
t8.new_ab()
t8.pitch_list("c 1 b 1")
t8.reach("FC6")


# Bot 8th
# Pitching: MIN #49 Adalberto Mejía
b8 = game.new_inning()

# Defensive change (MIN): #23 Mitch Garver replaces #26 Max Kepler (PH), playing C, batting 9th
b8.defensive_substitution(9, 23, "2")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("b c b c b f c")
b8.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("s")
b8.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("c b s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t9.pitching_substitution(46)

# 2. MIN #20 Eddie Rosario (X - X - X)
t9.new_ab()
t9.pitch_list("b c s s")
t9.out("K")

# 3. MIN #11 Jorge Polanco (X - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.reach("HBP")
t9.advance(2, "2 WP")
t9.thrown_out(3, "2 DP6-4", 3, 46)

# 4. MIN #2  Brian Dozier (X - X - 11)
t9.new_ab()
t9.pitch_list("b f c")
t9.wp()
t9.out("DP6-4")

# Winning team: BOS
# WP: BOS #17 Nathan Eovaldi
game.winning_pitcher(17)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: MIN
# LP: MIN #17 José Berríos
game.losing_pitcher(17, is_away_team=True)

# print(game)
game.generate_scorecard()
