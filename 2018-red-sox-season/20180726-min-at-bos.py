import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIN @ BOS, 2018-07-26
# https://www.baseball-reference.com/boxes/BOS/BOS201807260.shtml
# https://www.mlb.com/gameday/twins-vs-red-sox/2018/07/26/530950/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-26 19:11-22:10",
        "at": "Fenway Park, Boston, MA",
        "att": "37,439",
        "temp": "75F, Partly Cloudy",
        "wind": "8mph, Out To CF",
        "away": {
            "team": "Minnesota Twins",
            "starter": 44,
            "roster": {
                # Lineup
                7: "Joe Mauer",
                20: "Eddie Rosario",
                2: "Brian Dozier",
                5: "Eduardo Escobar",
                23: "Mitch Garver",
                36: "Robbie Grossman",
                26: "Max Kepler",
                16: "Ehire Adrianza",
                46: "Bobby Wilson",
                # Starting pitcher
                44: "Kyle Gibson",
                # Bench
                60: "Jake Cave",
                99: "Logan Morrison",
                11: "Jorge Polanco",
                # Bullpen
                54: "Ervin Santana",
                38: "Matt Belisle",
                31: "Lance Lynn",
                49: "Adalberto Mejía",
                68: "Matt Magill",
                39: "Trevor Hildenberger",
                12: "Jake Odorizzi",
                17: "José Berríos",
                56: "Fernando Rodney",
                57: "Ryan Pressly",
                55: "Taylor Rogers",
                32: "Zach Duke",
            },
            "lefties": [49, 55, 32],
            "lineup": [
                [7, "3"],
                [20, "7"],
                [2, "4"],
                [5, "5"],
                [23, "0"],
                [36, "9"],
                [26, "8"],
                [16, "6"],
                [46, "2"],
            ],
            "bench": [
                [60, "RF"],
                [99, "1B"],
                [11, "2B"],
            ],
            "bullpen": [54, 38, 31, 49, 68, 39, 12, 17, 56, 57, 55, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                25: "Steve Pearce",
                11: "Rafael Devers",
                23: "Blake Swihart",
                12: "Brock Holt",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                36: "Eduardo Núñez",
                18: "Mitch Moreland",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [61, 41, 31, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [25, "3"],
                [11, "5"],
                [23, "2"],
                [12, "4"],
                [19, "8"],
            ],
            "bench": [
                [36, "SS"],
                [18, "1B"],
                [3, "C"],
            ],
            "bullpen": [47, 22, 41, 31, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Marty Foster",
            "1B": "Joe West",
            "2B": "Mark Ripperger",
            "3B": "Doug Eddings",
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
# Pitching: BOS #61 Brian Johnson
t1 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(2, "2 1B")
t1.advance(3, "5 1B")
t1.thrown_out(4, "5 8-2", 2, 61)

# 2. MIN #20 Eddie Rosario (X - X - 7)
t1.new_ab()
t1.out("F8")

# 3. MIN #2  Brian Dozier (X - X - 7)
t1.new_ab()
t1.pitch_list("b d b c s")
t1.hit(1)
t1.advance(2, "5 8-2")
t1.advance(3, "23 WP")

# 4. MIN #5  Eduardo Escobar (X - 7 - 2)
t1.new_ab(is_risp=True)
t1.pitch_list("s f")
t1.hit(1)
t1.advance(2, "23 WP")

# 5. MIN #23 Mitch Garver (X - 2 - 5)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b b f f b")
t1.wp()
t1.reach("BB")

# 6. MIN #36 Robbie Grossman (2 - 5 - 23)
t1.new_ab(is_risp=True)
t1.pitch_list("c f b s")
t1.out("K")


# Bot 1st
# Pitching: MIN #44 Kyle Gibson
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.out("L8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f")
b1.hit(1)
b1.advance(3, "2 2B")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
b1.new_ab()
b1.pitch_list("b c b")
b1.hit(2)

# 5. BOS #25 Steve Pearce (28 - 2 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b b")
b1.reach("BB")

# 6. BOS #11 Rafael Devers (28 - 2 - 25)
b1.new_ab(is_risp=True)
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #61 Brian Johnson
t2 = game.new_inning()

# 7. MIN #26 Max Kepler (X - X - X)
t2.new_ab()
t2.pitch_list("c f b c")
t2.out("!K")

# 8. MIN #16 Ehire Adrianza (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")

# 9. MIN #46 Bobby Wilson (X - X - X)
t2.new_ab()
t2.pitch_list("f b c t")
t2.out("KT")


# Bot 2nd
# Pitching: MIN #44 Kyle Gibson
b2 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
b2.new_ab()
b2.pitch_list("f b s")
b2.hit(1)
b2.advance(2, "12 HBP")
b2.advance(3, "19 FC4-6")
b2.advance(4, "50 DP3-5")

# 8. BOS #12 Brock Holt (X - X - 23)
b2.new_ab()
b2.pitch_list("c b 1 1 f")
b2.reach("HBP")
b2.thrown_out(2, "19 FC4-6", 1, 44)

# 9. BOS #19 Jackie Bradley Jr. (X - 23 - 12)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.reach("FC4-6")
b2.advance(2, "50 DP3-5")
b2.thrown_out(3, "50 DP3-5", 3, 44)

# 1. BOS #50 Mookie Betts (23 - X - 19)
b2.new_ab(is_risp=True)
b2.pitch_list("b f b f 1 b 3")
b2.out("DP6-3-5", rbis=1)


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #61 Brian Johnson
t3 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
t3.new_ab()
t3.pitch_list("c f b")
t3.out("G5-3")

# 2. MIN #20 Eddie Rosario (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F8")

# 3. MIN #2  Brian Dozier (X - X - X)
t3.new_ab()
t3.pitch_list("b c b c b s")
t3.out("K")


# Bot 3rd
# Pitching: MIN #44 Kyle Gibson
b3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("s b")
b3.out("F7")

# 3. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("b s b b c f s")
b3.out("K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("b c s b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #61 Brian Johnson
t4 = game.new_inning()

# 4. MIN #5  Eduardo Escobar (X - X - X)
t4.new_ab()
t4.pitch_list("f b")
t4.out("G6-3")

# 5. MIN #23 Mitch Garver (X - X - X)
t4.new_ab()
t4.pitch_list("c b c b")
t4.out("F9")

# 6. MIN #36 Robbie Grossman (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G4-3")


# Bot 4th
# Pitching: MIN #44 Kyle Gibson
b4 = game.new_inning()

# 5. BOS #25 Steve Pearce (X - X - X)
b4.new_ab()
b4.pitch_list("b s b b")
b4.out("G5-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("c b s b")
b4.hit(1)
b4.advance(2, "23 G4-3")

# 7. BOS #23 Blake Swihart (X - X - 11)
b4.new_ab()
b4.pitch_list("c c")
b4.out("G4-3")

# 8. BOS #12 Brock Holt (X - 11 - X)
b4.new_ab(is_risp=True)
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# 7. MIN #26 Max Kepler (X - X - X)
t5.new_ab()
t5.pitch_list("b f")
t5.out("L8")

# 8. MIN #16 Ehire Adrianza (X - X - X)
t5.new_ab()
t5.pitch_list("b b c b f f f f c")
t5.out("!K")

# 9. MIN #46 Bobby Wilson (X - X - X)
t5.new_ab()
t5.pitch_list("c f")
t5.out("F8")


# Bot 5th
# Pitching: MIN #44 Kyle Gibson
b5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b f b s")
b5.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("c b f s")
b5.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b5.new_ab()
b5.pitch_list("b 1")
b5.out("G1")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #61 Brian Johnson
t6 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
t6.new_ab()
t6.out("L7")

# 2. MIN #20 Eddie Rosario (X - X - X)
t6.new_ab()
t6.pitch_list("b s b b b")
t6.reach("BB")
t6.advance(2, "2 1B")
t6.thrown_out(4, "2 8-5-4-2", 2, 61)

# 3. MIN #2  Brian Dozier (X - X - 20)
t6.new_ab()
t6.pitch_list("c 1 1")
t6.hit(1)
t6.advance(2, "T")

# 4. MIN #5  Eduardo Escobar (X - 2 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("f s d b d d")
t6.reach("BB")

# Pitching change (BOS): #37 Heath Hembree replaces #61 Brian Johnson
t6.pitching_substitution(37)

# 5. MIN #23 Mitch Garver (X - 2 - 5)
t6.new_ab(is_risp=True)
t6.pitch_list("b s t")
t6.out("G4-3")


# Bot 6th
# Pitching: MIN #44 Kyle Gibson
b6 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f b f s")
b6.out("K")

# 5. BOS #25 Steve Pearce (X - X - X)
b6.new_ab()
b6.pitch_list("b b c s b c")
b6.out("!K")

# 6. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# 6. MIN #36 Robbie Grossman (X - X - X)
t7.new_ab()
t7.pitch_list("c f b")
t7.hit(1)
t7.advance(3, "26 1B")
t7.advance(4, "16 DP4-6-3")

# 7. MIN #26 Max Kepler (X - X - 36)
t7.new_ab()
t7.pitch_list("d b f b c")
t7.hit(1)
t7.thrown_out(2, "16 DP4-6-3", 1, 37)

# 8. MIN #16 Ehire Adrianza (36 - X - 26)
t7.new_ab(is_risp=True)
t7.pitch_list("l s b b 1")
t7.out("DP4-6-3")

# 9. MIN #46 Bobby Wilson (X - X - X)
t7.new_ab()
t7.pitch_list("s f b")
t7.hit(1)

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
t7.pitching_substitution(32)

# 1. MIN #7  Joe Mauer (X - X - 46)
t7.new_ab()
t7.pitch_list("c d f f b f s")
t7.out("K")


# Bot 7th
# Pitching: MIN #44 Kyle Gibson
b7 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.out("L9")

# 8. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("L3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c b s f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# 2. MIN #20 Eddie Rosario (X - X - X)
t8.new_ab()
t8.pitch_list("s f b s")
t8.out("K")

# 3. MIN #2  Brian Dozier (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b b")
t8.reach("BB")
t8.advance(2, "5 SB")
t8.advance(4, "23 2B")

# 4. MIN #5  Eduardo Escobar (X - X - 2)
t8.new_ab()
t8.pitch_list("c s s")
t8.out("K")

# 5. MIN #23 Mitch Garver (X - 2 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b c b")
t8.hit(2, rbis=1)

# 6. MIN #36 Robbie Grossman (X - 23 - X)
t8.new_ab(is_risp=True)
t8.out("F7")


# Bot 8th
# Pitching: MIN #44 Kyle Gibson
b8 = game.new_inning()

# Defensive change (MIN): #60 Jake Cave replaces #36 Robbie Grossman (RF), playing CF, batting 6th
b8.defensive_substitution(6, 60, "8")

# Defensive switch (MIN): #26 Max Kepler moves to RF
b8.defensive_switch(26, "9")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("b b f f f b")
b8.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b s b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #70 Ryan Brasier
t9 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #32 Matt Barnes
t9.pitching_substitution(70)

# 7. MIN #26 Max Kepler (X - X - X)
t9.new_ab()
t9.pitch_list("f b")
t9.out("P6")

# 8. MIN #16 Ehire Adrianza (X - X - X)
t9.new_ab()
t9.pitch_list("f b")
t9.out("L8")

# 9. MIN #46 Bobby Wilson (X - X - X)
t9.new_ab()
t9.pitch_list("s f s")
t9.out("K")


# Bot 9th
# Pitching: MIN #56 Fernando Rodney
b9 = game.new_inning()

# Pitching change (MIN): #56 Fernando Rodney replaces #44 Kyle Gibson
b9.pitching_substitution(56)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.hit(1)
b9.advance(2, "25 G2-3")
b9.advance(3, "12 BB")

# 5. BOS #25 Steve Pearce (X - X - 2)
b9.new_ab()
b9.pitch_list("c")
b9.out("G2-3")

# 6. BOS #11 Rafael Devers (X - 2 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c f")
b9.out("(F)P5")

# 7. BOS #23 Blake Swihart (X - 2 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b d f b b")
b9.reach("BB")
b9.advance(2, "12 BB")

# 8. BOS #12 Brock Holt (X - 2 - 23)
b9.new_ab(is_risp=True)
b9.pitch_list("b b c f d d")
b9.reach("BB")

# 9. BOS #19 Jackie Bradley Jr. (2 - 23 - 12)
b9.new_ab(is_risp=True)
b9.pitch_list("b b d c c s")
b9.out("K")

# Winning team: MIN
# WP: MIN #44 Kyle Gibson
game.winning_pitcher(44, is_away_team=True)
# SV: MIN #56 Fernando Rodney
game.save_pitcher(56, is_away_team=True)

# Loser team: BOS
# LP: BOS #32 Matt Barnes
game.losing_pitcher(32)

# print(game)
game.generate_scorecard()
