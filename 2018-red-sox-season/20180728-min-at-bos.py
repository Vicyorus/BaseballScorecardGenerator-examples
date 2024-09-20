import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIN @ BOS, 2018-07-28
# https://www.baseball-reference.com/boxes/BOS/BOS201807280.shtml
# https://www.mlb.com/gameday/twins-vs-red-sox/2018/07/28/530977/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-28 19:10-22:38",
        "at": "Fenway Park, Boston, MA",
        "att": "36,798",
        "temp": "82F, Partly Cloudy",
        "wind": "17mph, Out To LF",
        "away": {
            "team": "Minnesota Twins",
            "starter": 12,
            "roster": {
                # Lineup
                7: "Joe Mauer",
                20: "Eddie Rosario",
                11: "Jorge Polanco",
                2: "Brian Dozier",
                99: "Logan Morrison",
                22: "Miguel Sanó",
                36: "Robbie Grossman",
                23: "Mitch Garver",
                60: "Jake Cave",
                # Starting pitcher
                12: "Jake Odorizzi",
                # Bench
                16: "Ehire Adrianza",
                46: "Bobby Wilson",
                26: "Max Kepler",
                # Bullpen
                54: "Ervin Santana",
                38: "Matt Belisle",
                58: "Gabriel Moya",
                31: "Lance Lynn",
                49: "Adalberto Mejía",
                68: "Matt Magill",
                39: "Trevor Hildenberger",
                17: "José Berríos",
                56: "Fernando Rodney",
                55: "Taylor Rogers",
                32: "Zach Duke",
                44: "Kyle Gibson",
            },
            "lefties": [58, 49, 55, 32],
            "lineup": [
                [7, "3"],
                [20, "7"],
                [11, "6"],
                [2, "4"],
                [99, "0"],
                [22, "5"],
                [36, "9"],
                [23, "2"],
                [60, "8"],
            ],
            "bench": [
                [16, "3B"],
                [46, "C"],
                [26, "RF"],
            ],
            "bullpen": [54, 38, 58, 31, 49, 68, 39, 17, 56, 55, 32, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                25: "Steve Pearce",
                23: "Blake Swihart",
                12: "Brock Holt",
                # Bullpen
                47: "Tyler Thornburg",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [24, 31, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [23, "C"],
                [12, "2B"],
            ],
            "bullpen": [47, 24, 46, 76, 70, 56, 31, 61, 17, 32, 37],
        },
        "umpires": {
            "HP": "Mark Ripperger",
            "1B": "Doug Eddings",
            "2B": "Marty Foster",
            "3B": "Joe West",
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
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
t1.new_ab()
t1.pitch_list("c t")
t1.out("G6-3")

# 2. MIN #20 Eddie Rosario (X - X - X)
t1.new_ab()
t1.pitch_list("f f f")
t1.out("G3-1")

# 3. MIN #11 Jorge Polanco (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b c")
t1.out("!K")


# Bot 1st
# Pitching: MIN #12 Jake Odorizzi
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c f")
b1.hit(1)
b1.advance(2, "28 1B")
b1.advance(4, "18 1B")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b1.new_ab()
b1.hit(1)
b1.advance(2, "18 1B")
b1.advance(3, "2 F8")

# 4. BOS #18 Mitch Moreland (X - 16 - 28)
b1.new_ab()
b1.pitch_list("b f b b f f")
b1.hit(1, rbis=1)
b1.advance(2, "11 1B")

# 5. BOS #2  Xander Bogaerts (X - 28 - 18)
b1.new_ab()
b1.pitch_list("d c f f")
b1.out("F8")

# 6. BOS #11 Rafael Devers (28 - X - 18)
b1.new_ab()
b1.hit(1)

# 7. BOS #36 Eduardo Núñez (28 - 18 - 11)
b1.new_ab()
b1.pitch_list("c")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 4. MIN #2  Brian Dozier (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G5-3")

# 5. MIN #99 Logan Morrison (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b")
t2.hit(4)

# 6. MIN #22 Miguel Sanó (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G5-3")

# 7. MIN #36 Robbie Grossman (X - X - X)
t2.new_ab()
t2.pitch_list("f b c c")
t2.out("!K")


# Bot 2nd
# Pitching: MIN #12 Jake Odorizzi
b2 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("c f b f b f b f f")
b2.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("s c s")
b2.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("c c b f b")
b2.out("G2-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 8. MIN #23 Mitch Garver (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b b")
t3.out("G3-1")

# 9. MIN #60 Jake Cave (X - X - X)
t3.new_ab()
t3.pitch_list("c c b f")
t3.hit(1)
t3.advance(2, "7 1B")
t3.advance(4, "11 3B")

# 1. MIN #7  Joe Mauer (X - X - 60)
t3.new_ab()
t3.pitch_list("c b b 1 f f")
t3.hit(1)
t3.advance(4, "11 3B")

# 2. MIN #20 Eddie Rosario (X - 60 - 7)
t3.new_ab()
t3.pitch_list("b f s s")
t3.out("K")

# 3. MIN #11 Jorge Polanco (X - 60 - 7)
t3.new_ab()
t3.pitch_list("b")
t3.hit(3, rbis=2)
t3.advance(4, "2 1B")

# 4. MIN #2  Brian Dozier (11 - X - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.hit(1, rbis=1)

# 5. MIN #99 Logan Morrison (X - X - 2)
t3.new_ab()
t3.pitch_list("s")
t3.out("B1-3")


# Bot 3rd
# Pitching: MIN #12 Jake Odorizzi
b3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b f")
b3.out("G6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("c f b s")
b3.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.out("L5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 6. MIN #22 Miguel Sanó (X - X - X)
t4.new_ab()
t4.pitch_list("b b c f b f c")
t4.out("!K")

# 7. MIN #36 Robbie Grossman (X - X - X)
t4.new_ab()
t4.error(4)
t4.reach("E4")

# 8. MIN #23 Mitch Garver (X - X - 36)
t4.new_ab()
t4.pitch_list("c b c")
t4.out("L9")

# 9. MIN #60 Jake Cave (X - X - 36)
t4.new_ab()
t4.out("L6")


# Bot 4th
# Pitching: MIN #12 Jake Odorizzi
b4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c b f f")
b4.out("F8")

# 6. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b b s f")
b4.hit(2)
b4.advance(4, "19 3B")

# 7. BOS #36 Eduardo Núñez (X - 11 - X)
b4.new_ab()
b4.pitch_list("b b c b s b")
b4.reach("BB")
b4.advance(4, "19 3B")

# 8. BOS #3  Sandy León (X - 11 - 36)
b4.new_ab()
b4.pitch_list("f b")
b4.out("F8")

# 9. BOS #19 Jackie Bradley Jr. (X - 11 - 36)
b4.new_ab()
b4.hit(3, rbis=2)
b4.advance(4, "50 2B")

# 1. BOS #50 Mookie Betts (19 - X - X)
b4.new_ab()
b4.pitch_list("b c f d")
b4.hit(2, rbis=1)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
t5.new_ab()
t5.pitch_list("c b b f f")
t5.out("L7")

# 2. MIN #20 Eddie Rosario (X - X - X)
t5.new_ab()
t5.out("L8")

# 3. MIN #11 Jorge Polanco (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G5-3")


# Bot 5th
# Pitching: MIN #12 Jake Odorizzi
b5 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(4)

# 4. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("b s b c t")
b5.out("KT")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.hit(1)

# 6. BOS #11 Rafael Devers (X - X - 2)
b5.new_ab()
b5.pitch_list("b s 1 t s")
b5.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
b5.new_ab()
b5.pitch_list("f b f 1 s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 4. MIN #2  Brian Dozier (X - X - X)
t6.new_ab()
t6.pitch_list("b c c f b f b f b")
t6.reach("BB")
t6.advance(2, "99 PB")
t6.advance(3, "36 SB")

# 5. MIN #99 Logan Morrison (X - X - 2)
t6.new_ab()
t6.pitch_list("b f b b c")
t6.pb()
t6.out("F8")

# 6. MIN #22 Miguel Sanó (X - 2 - X)
t6.new_ab()
t6.pitch_list("b b b c f f f s")
t6.out("K")

# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello
t6.pitching_substitution(37)

# 7. MIN #36 Robbie Grossman (X - 2 - X)
t6.new_ab()
t6.pitch_list("b c s d")
t6.out("G6-3")


# Bot 6th
# Pitching: MIN #58 Gabriel Moya
b6 = game.new_inning()

# Pitching change (MIN): #58 Gabriel Moya replaces #12 Jake Odorizzi
b6.pitching_substitution(58)

# 8. BOS #3  Sandy León (X - X - X)
b6.new_ab()
b6.hit(2)
b6.advance(3, "16 WP")
b6.advance(4, "16 1B")

# 9. BOS #19 Jackie Bradley Jr. (X - 3 - X)
b6.new_ab()
b6.pitch_list("b s b c f f b f d")
b6.reach("BB")
b6.advance(2, "16 WP")
b6.advance(3, "16 1B")

# 1. BOS #50 Mookie Betts (X - 3 - 19)
b6.new_ab()
b6.pitch_list("c b b f c")
b6.out("!K")

# 2. BOS #16 Andrew Benintendi (X - 3 - 19)
b6.new_ab()
b6.pitch_list("b s b")
b6.wp()
b6.hit(1, rbis=1)
b6.advance(2, "18 SB")

# Pitching change (MIN): #68 Matt Magill replaces #58 Gabriel Moya
b6.pitching_substitution(68)

# 3. BOS #28 J.D. Martinez (19 - X - 16)
b6.new_ab()
b6.pitch_list("f 1 s b s")
b6.out("K")

# 4. BOS #18 Mitch Moreland (19 - X - 16)
b6.new_ab()
b6.pitch_list("b f b s f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# 8. MIN #23 Mitch Garver (X - X - X)
t7.new_ab()
t7.pitch_list("c b f s")
t7.out("K")

# 9. MIN #60 Jake Cave (X - X - X)
t7.new_ab()
t7.pitch_list("b f c b")
t7.out("F8")

# 1. MIN #7  Joe Mauer (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)

# 2. MIN #20 Eddie Rosario (X - X - 7)
t7.new_ab()
t7.pitch_list("s b s")
t7.out("G3")


# Bot 7th
# Pitching: MIN #68 Matt Magill
b7 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c f b s")
b7.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.out("G6-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.hit(3)

# 8. BOS #3  Sandy León (36 - X - X)
b7.new_ab()
b7.pitch_list("b c b b c")
b7.out("G1-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #47 Tyler Thornburg
t8 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #37 Heath Hembree
t8.pitching_substitution(47)

# 3. MIN #11 Jorge Polanco (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b")
t8.out("G3")

# 4. MIN #2  Brian Dozier (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b s")
t8.out("K")

# 5. MIN #99 Logan Morrison (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G4-3")


# Bot 8th
# Pitching: MIN #68 Matt Magill
b8 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b b")
b8.reach("BB")
b8.advance(4, "50 2B")

# 1. BOS #50 Mookie Betts (X - X - 19)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2, rbis=1)
b8.advance(3, "18 SB")
b8.advance(4, "11 BB")

# Pitching change (MIN): #55 Taylor Rogers replaces #68 Matt Magill
b8.pitching_substitution(55)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b8.new_ab()
b8.pitch_list("c f f s")
b8.out("K")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
b8.new_ab()
b8.pitch_list("v v v v")
b8.reach("IBB")
b8.advance(2, "2 IBB")
b8.advance(3, "11 BB")
b8.advance(4, "36 2B")

# 4. BOS #18 Mitch Moreland (X - 50 - 28)
b8.new_ab()
b8.pitch_list("c b t b s")
b8.out("K")

# 5. BOS #2  Xander Bogaerts (50 - X - 28)
b8.new_ab()
b8.pitch_list("v v v v")
b8.reach("IBB")
b8.advance(2, "11 BB")
b8.advance(4, "36 2B")

# 6. BOS #11 Rafael Devers (50 - 28 - 2)
b8.new_ab()
b8.pitch_list("b b b c c f f b")
b8.reach("BB", rbis=1)
b8.advance(3, "36 2B")
# Offensive change (BOS): Pinch-runner #12 Brock Holt replaces #11 Rafael Devers
b8.offensive_substitution(6, 12, "PR")
b8.atbase("PR")

# 7. BOS #36 Eduardo Núñez (28 - 2 - 11)
b8.new_ab()
b8.hit(2, rbis=2)

# 8. BOS #3  Sandy León (11 - 36 - X)
b8.new_ab()
b8.pitch_list("c c b f f d c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #56 Joe Kelly
t9 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #47 Tyler Thornburg
t9.pitching_substitution(56)

# Defensive switch (BOS): #12 Brock Holt moves to 2B
t9.defensive_switch(12, "4")

# Defensive switch (BOS): #36 Eduardo Núñez moves to 3B
t9.defensive_switch(36, "5")

# 6. MIN #22 Miguel Sanó (X - X - X)
t9.new_ab()
t9.pitch_list("b c f b s")
t9.out("K")

# 7. MIN #36 Robbie Grossman (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.pb()
t9.reach("K")
t9.advance(2, "23 1B")

# 8. MIN #23 Mitch Garver (X - X - 36)
t9.new_ab()
t9.pitch_list("b c b")
t9.hit(1)
t9.thrown_out(2, "60 DP6-3", 2, 56)

# 9. MIN #60 Jake Cave (X - 36 - 23)
t9.new_ab()
t9.pitch_list("c")
t9.out("DP6-3")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22)

# Loser team: MIN
# LP: MIN #12 Jake Odorizzi
game.losing_pitcher(12, is_away_team=True)

# print(game)
game.generate_scorecard()
