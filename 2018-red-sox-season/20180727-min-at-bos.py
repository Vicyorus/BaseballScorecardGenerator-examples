import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIN @ BOS, 2018-07-27
# https://www.baseball-reference.com/boxes/BOS/BOS201807270.shtml
# https://www.mlb.com/gameday/twins-vs-red-sox/2018/07/27/530962/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-27 19:11-22:37",
        "at": "Fenway Park, Boston, MA",
        "att": "37,273",
        "temp": "83F, Partly Cloudy",
        "wind": "13mph, Out To LF",
        "away": {
            "team": "Minnesota Twins",
            "starter": 31,
            "roster": {
                # Lineup
                11: "Jorge Polanco",
                20: "Eddie Rosario",
                2: "Brian Dozier",
                23: "Mitch Garver",
                99: "Logan Morrison",
                16: "Ehire Adrianza",
                26: "Max Kepler",
                36: "Robbie Grossman",
                60: "Jake Cave",
                # Starting pitcher
                31: "Lance Lynn",
                # Bench
                7: "Joe Mauer",
                46: "Bobby Wilson",
                # Bullpen
                12: "Jake Odorizzi",
                17: "José Berríos",
                54: "Ervin Santana",
                38: "Matt Belisle",
                56: "Fernando Rodney",
                55: "Taylor Rogers",
                49: "Adalberto Mejía",
                32: "Zach Duke",
                68: "Matt Magill",
                44: "Kyle Gibson",
                39: "Trevor Hildenberger",
            },
            "lefties": [55, 49, 32],
            "lineup": [
                [11, "6"],
                [20, "7"],
                [2, "4"],
                [23, "2"],
                [99, "3"],
                [16, "5"],
                [26, "9"],
                [36, "0"],
                [60, "8"],
            ],
            "bench": [
                [7, "C"],
                [46, "C"],
            ],
            "bullpen": [12, 17, 54, 38, 56, 55, 49, 32, 68, 44, 39],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                25: "Steve Pearce",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                22: "Rick Porcello",
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
            "lefties": [41, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [25, "3"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
            ],
            "bullpen": [47, 22, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Joe West",
            "1B": "Mark Ripperger",
            "2B": "Doug Eddings",
            "3B": "Marty Foster",
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
# Pitching: BOS #41 Chris Sale
t1 = game.new_inning()

# 1. MIN #11 Jorge Polanco (X - X - X)
t1.new_ab()
t1.pitch_list("c f s")
t1.out("K")

# 2. MIN #20 Eddie Rosario (X - X - X)
t1.new_ab()
t1.pitch_list("s")
t1.hit(1)

# 3. MIN #2  Brian Dozier (X - X - 20)
t1.new_ab()
t1.pitch_list("f c f f b s")
t1.out("K")

# 4. MIN #23 Mitch Garver (X - X - 20)
t1.new_ab()
t1.pitch_list("1 b c s t")
t1.out("KT")


# Bot 1st
# Pitching: MIN #31 Lance Lynn
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c c b f b")
b1.hit(1)

# 4. BOS #2  Xander Bogaerts (X - X - 28)
b1.new_ab()
b1.pitch_list("c c f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 5. MIN #99 Logan Morrison (X - X - X)
t2.new_ab()
t2.pitch_list("c b b c f b")
t2.hit(1)

# 6. MIN #16 Ehire Adrianza (X - X - 99)
t2.new_ab()
t2.pitch_list("c c c")
t2.out("!K")

# 7. MIN #26 Max Kepler (X - X - 99)
t2.new_ab()
t2.pitch_list("c b c s")
t2.out("K")

# 8. MIN #36 Robbie Grossman (X - X - 99)
t2.new_ab()
t2.out("G1")


# Bot 2nd
# Pitching: MIN #31 Lance Lynn
b2 = game.new_inning()

# 5. BOS #25 Steve Pearce (X - X - X)
b2.new_ab()
b2.pitch_list("c c b b")
b2.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("f b s")
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 9. MIN #60 Jake Cave (X - X - X)
t3.new_ab()
t3.pitch_list("b s f b")
t3.out("G6-3")

# 1. MIN #11 Jorge Polanco (X - X - X)
t3.new_ab()
t3.pitch_list("c s f")
t3.hit(1)
t3.thrown_out(2, "20 FC5-6", 2, 41)

# 2. MIN #20 Eddie Rosario (X - X - 11)
t3.new_ab()
t3.pitch_list("f")
t3.reach("FC5-6")
t3.advance(2, "2 WP")

# 3. MIN #2  Brian Dozier (X - X - 20)
t3.new_ab()
t3.pitch_list("b")
t3.wp()
t3.out("P3")


# Bot 3rd
# Pitching: MIN #31 Lance Lynn
b3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.thrown_out(2, "50 FC5-4", 2, 31)

# 1. BOS #50 Mookie Betts (X - X - 19)
b3.new_ab()
b3.pitch_list("b s c f 1 1 f f b")
b3.reach("FC5-4")
b3.advance(2, "16 SB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("s b b b f f")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 4. MIN #23 Mitch Garver (X - X - X)
t4.new_ab()
t4.pitch_list("c b c b")
t4.out("L7")

# 5. MIN #99 Logan Morrison (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.out("G6-3")

# 6. MIN #16 Ehire Adrianza (X - X - X)
t4.new_ab()
t4.pitch_list("f b s b b b")
t4.reach("BB")
t4.advance(2, "26 HBP")
t4.advance(3, "36 BB")

# 7. MIN #26 Max Kepler (X - X - 16)
t4.new_ab()
t4.reach("HBP")
t4.advance(2, "36 BB")

# 8. MIN #36 Robbie Grossman (X - 16 - 26)
t4.new_ab()
t4.pitch_list("b c f b b b")
t4.reach("BB")

# 9. MIN #60 Jake Cave (16 - 26 - 36)
t4.new_ab()
t4.pitch_list("b b f f b f f s")
t4.out("K")


# Bot 4th
# Pitching: MIN #31 Lance Lynn
b4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.out("F9")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b c s s")
b4.out("K")

# 5. BOS #25 Steve Pearce (X - X - X)
b4.new_ab()
b4.reach("HBP")
b4.advance(2, "11 WP")

# 6. BOS #11 Rafael Devers (X - X - 25)
b4.new_ab()
b4.pitch_list("s b f b")
b4.wp()
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 1. MIN #11 Jorge Polanco (X - X - X)
t5.new_ab()
t5.pitch_list("c f s")
t5.out("K")

# 2. MIN #20 Eddie Rosario (X - X - X)
t5.new_ab()
t5.pitch_list("c c f")
t5.out("P3")

# 3. MIN #2  Brian Dozier (X - X - X)
t5.new_ab()
t5.pitch_list("c b s f b c")
t5.out("!K")


# Bot 5th
# Pitching: MIN #31 Lance Lynn
b5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(2)
b5.advance(3, "3 L9")
b5.advance(4, "19 HR")

# 8. BOS #3  Sandy León (X - 36 - X)
b5.new_ab()
b5.pitch_list("b b f")
b5.out("L9")

# 9. BOS #19 Jackie Bradley Jr. (36 - X - X)
b5.new_ab()
b5.pitch_list("c d b")
b5.hit(4, rbis=2)

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b b")
b5.reach("BB")
b5.advance(2, "16 G4-3")
b5.advance(3, "28 WP")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b5.new_ab()
b5.pitch_list("1 1 1 b b f b")
b5.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
b5.new_ab()
b5.pitch_list("f s b b t")
b5.wp()
b5.out("KT")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 Chris Sale
t6 = game.new_inning()

# 4. MIN #23 Mitch Garver (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c f")
t6.out("G6-3")

# 5. MIN #99 Logan Morrison (X - X - X)
t6.new_ab()
t6.pitch_list("b c c b b s")
t6.out("K")

# 6. MIN #16 Ehire Adrianza (X - X - X)
t6.new_ab()
t6.pitch_list("s f s")
t6.out("K")


# Bot 6th
# Pitching: MIN #31 Lance Lynn
b6 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G5-3")

# 5. BOS #25 Steve Pearce (X - X - X)
b6.new_ab()
b6.pitch_list("b f b f f")
b6.hit(1)
b6.advance(2, "36 1B")

# 6. BOS #11 Rafael Devers (X - X - 25)
b6.new_ab()
b6.pitch_list("b f b")
b6.out("P6")

# 7. BOS #36 Eduardo Núñez (X - X - 25)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)

# 8. BOS #3  Sandy León (X - 25 - 36)
b6.new_ab()
b6.pitch_list("b b d c f")
b6.out("L7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #70 Ryan Brasier
t7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #41 Chris Sale
t7.pitching_substitution(70)

# 7. MIN #26 Max Kepler (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(2)
t7.advance(3, "36 G1-3")
t7.advance(4, "60 E4")

# 8. MIN #36 Robbie Grossman (X - 26 - X)
t7.new_ab()
t7.pitch_list("s b f")
t7.out("G1-3")

# 9. MIN #60 Jake Cave (26 - X - X)
t7.new_ab()
t7.pitch_list("d")
t7.error(4)
t7.reach("E4", end_base=2, rbis=1)
t7.advance(3, "11 1B")

# 1. MIN #11 Jorge Polanco (X - 60 - X)
t7.new_ab()
t7.pitch_list("c f b d")
t7.hit(1)
t7.thrown_out(2, "20 DP3-6-3", 2, 70)

# 2. MIN #20 Eddie Rosario (60 - X - 11)
t7.new_ab()
t7.pitch_list("1 c 1")
t7.out("DP3-6-3")


# Bot 7th
# Pitching: MIN #55 Taylor Rogers
b7 = game.new_inning()

# Pitching change (MIN): #55 Taylor Rogers replaces #31 Lance Lynn
b7.pitching_substitution(55)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c f b f b s")
b7.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("c c b")
b7.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("f c b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #70 Ryan Brasier
t8.pitching_substitution(32)

# 3. MIN #2  Brian Dozier (X - X - X)
t8.new_ab()
t8.out("G6-3")

# 4. MIN #23 Mitch Garver (X - X - X)
t8.new_ab()
t8.pitch_list("b c b b c f f f s")
t8.out("K")

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t8.pitching_substitution(46)

# 5. MIN #99 Logan Morrison (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")

# Offensive change (MIN): Pinch-hitter #7 Joe Mauer replaces #16 Ehire Adrianza, batting 6th
t8.offensive_substitution(6, 7, "PH")

# 6. MIN #7  Joe Mauer (X - X - 99)
t8.new_ab()
t8.out("F7")


# Bot 8th
# Pitching: MIN #39 Trevor Hildenberger
b8 = game.new_inning()

# Pitching change (MIN): #39 Trevor Hildenberger replaces #55 Taylor Rogers
b8.pitching_substitution(39)

# Defensive switch (MIN): #20 Eddie Rosario moves to 3B
b8.defensive_switch(20, "5")

# Defensive switch (MIN): #99 Logan Morrison moves to LF
b8.defensive_switch(99, "7")

# Defensive switch (MIN): #7 Joe Mauer moves to 1B
b8.defensive_switch(7, "3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b f f s")
b8.out("K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G5-3")

# 5. BOS #25 Steve Pearce (X - X - X)
b8.new_ab()
b8.pitch_list("c s b f b b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# 7. MIN #26 Max Kepler (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("L7")

# 8. MIN #36 Robbie Grossman (X - X - X)
t9.new_ab()
t9.pitch_list("c b b c b b")
t9.reach("BB")
t9.advance(2, "11 WP")
t9.advance(4, "20 2B")

# 9. MIN #60 Jake Cave (X - X - 36)
t9.new_ab()
t9.pitch_list("b b t c f f b")
t9.out("L7")

# 1. MIN #11 Jorge Polanco (X - X - 36)
t9.new_ab()
t9.pitch_list("1 c b f d d b")
t9.wp()
t9.reach("BB")
t9.advance(4, "20 2B")

# 2. MIN #20 Eddie Rosario (X - 36 - 11)
t9.new_ab()
t9.pitch_list("f")
t9.hit(2, rbis=2)

# 3. MIN #2  Brian Dozier (X - 20 - X)
t9.new_ab()
t9.pitch_list("c f d")
t9.out("G4-3")


# Bot 9th
# Pitching: MIN #56 Fernando Rodney
b9 = game.new_inning()

# Pitching change (MIN): #56 Fernando Rodney replaces #39 Trevor Hildenberger
b9.pitching_substitution(56)

# 6. BOS #11 Rafael Devers (X - X - X)
b9.new_ab()
b9.pitch_list("s b b")
b9.hit(4, rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("c f b f f b s")
b9.out("K")

# 8. BOS #3  Sandy León (X - X - X)
b9.new_ab()
b9.pitch_list("c b b b s")
b9.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b9.new_ab()
b9.pitch_list("s c b b s")
b9.out("K")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #47 Tyler Thornburg
t10 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #46 Craig Kimbrel
t10.pitching_substitution(47)

# 4. MIN #23 Mitch Garver (X - X - X)
t10.new_ab()
t10.pitch_list("c")
t10.out("G5-3")

# 5. MIN #99 Logan Morrison (X - X - X)
t10.new_ab()
t10.pitch_list("b c s c")
t10.out("!K")

# 6. MIN #7  Joe Mauer (X - X - X)
t10.new_ab()
t10.pitch_list("c b f")
t10.out("F8")


# Bot 10th
# Pitching: MIN #38 Matt Belisle
b10 = game.new_inning()

# Pitching change (MIN): #38 Matt Belisle replaces #56 Fernando Rodney
b10.pitching_substitution(38)

# 1. BOS #50 Mookie Betts (X - X - X)
b10.new_ab()
b10.pitch_list("c")
b10.hit(4, rbis=1)

# Winning team: BOS
# WP: BOS #47 Tyler Thornburg
game.winning_pitcher(47)

# Loser team: MIN
# LP: MIN #38 Matt Belisle
game.losing_pitcher(38, is_away_team=True)

# print(game)
game.generate_scorecard()
