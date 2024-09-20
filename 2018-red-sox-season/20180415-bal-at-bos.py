import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-04-15
# https://www.baseball-reference.com/boxes/BOS/BOS201804150.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/04/15/529629/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "extended_roster": True,
        "scorer": "Vicyorus",
        "date": "2018-04-15 13:05-15:59",
        "at": "Fenway Park, Boston, MA",
        "att": "32,489",
        "temp": "34F, Cloudy",
        "wind": "23mph, In From CF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 605164,
            "roster": {
                # Lineup
                641820: {"jersey": 42, "name": "Trey Mancini"},
                502226: {"jersey": 42, "name": "Craig Gentry"},
                592518: {"jersey": 42, "name": "Manny Machado"},
                430945: {"jersey": 42, "name": "Adam Jones"},
                502143: {"jersey": 42, "name": "Danny Valencia"},
                448801: {"jersey": 42, "name": "Chris Davis"},
                542921: {"jersey": 42, "name": "Tim Beckham"},
                623993: {"jersey": 42, "name": "Anthony Santander"},
                543376: {"jersey": 42, "name": "Caleb Joseph"},
                # Starting pitcher
                605164: {"jersey": 42, "name": "Dylan Bundy"},
                # Bench
                476883: {"jersey": 42, "name": "Pedro Alvarez"},
                622713: {"jersey": 42, "name": "Engelb Vielma"},
                642082: {"jersey": 42, "name": "Chance Sisco"},
                # Bullpen
                502171: {"jersey": 42, "name": "Alex Cobb"},
                542947: {"jersey": 42, "name": "Richard Bleier"},
                501957: {"jersey": 42, "name": "Chris Tillman"},
                605276: {"jersey": 42, "name": "David Hess"},
                592332: {"jersey": 42, "name": "Kevin Gausman"},
                503285: {"jersey": 42, "name": "Darren O'Day"},
                488768: {"jersey": 42, "name": "Andrew Cashner"},
                571710: {"jersey": 42, "name": "Mychal Givens"},
                605541: {"jersey": 42, "name": "Mike Wright Jr."},
                606478: {"jersey": 42, "name": "Pedro Araújo"},
                612434: {"jersey": 42, "name": "Miguel Castro"},
                542960: {"jersey": 42, "name": "Brad Brach"},
            },
            "lefties": [542947],
            "lineup": [
                [641820, "7"],
                [502226, "8"],
                [592518, "6"],
                [430945, "0"],
                [502143, "5"],
                [448801, "3"],
                [542921, "4"],
                [623993, "9"],
                [543376, "2"],
            ],
            "bench": [
                [476883, "3B"],
                [622713, "SS"],
                [642082, "C"],
            ],
            "bullpen": [
                502171,
                542947,
                501957,
                605276,
                592332,
                503285,
                488768,
                571710,
                605541,
                606478,
                612434,
                542960,
            ],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 519242,
            "roster": {
                # Lineup
                598265: {"jersey": 42, "name": "Jackie Bradley Jr."},
                643217: {"jersey": 42, "name": "Andrew Benintendi"},
                434670: {"jersey": 42, "name": "Hanley Ramirez"},
                502110: {"jersey": 42, "name": "J.D. Martinez"},
                519048: {"jersey": 42, "name": "Mitch Moreland"},
                646240: {"jersey": 42, "name": "Rafael Devers"},
                543877: {"jersey": 42, "name": "Christian Vázquez"},
                571788: {"jersey": 42, "name": "Brock Holt"},
                624407: {"jersey": 42, "name": "Tzu-Wei Lin"},
                # Starting pitcher
                519242: {"jersey": 42, "name": "Chris Sale"},
                # Bench
                456488: {"jersey": 42, "name": "Eduardo Núñez"},
                596119: {"jersey": 42, "name": "Blake Swihart"},
                605141: {"jersey": 42, "name": "Mookie Betts"},
                506702: {"jersey": 42, "name": "Sandy León"},
                # Bullpen
                593958: {"jersey": 42, "name": "Eduardo Rodriguez"},
                605476: {"jersey": 42, "name": "Carson Smith"},
                519144: {"jersey": 42, "name": "Rick Porcello"},
                598271: {"jersey": 42, "name": "Brian Johnson"},
                592390: {"jersey": 42, "name": "Heath Hembree"},
                456034: {"jersey": 42, "name": "David Price"},
                518886: {"jersey": 42, "name": "Craig Kimbrel"},
                584171: {"jersey": 42, "name": "Hector Velázquez"},
                519393: {"jersey": 42, "name": "Marcus Walden"},
                523260: {"jersey": 42, "name": "Joe Kelly"},
                598264: {"jersey": 42, "name": "Matt Barnes"},
            },
            "lefties": [519242, 593958, 598271, 456034],
            "lineup": [
                [598265, "9"],
                [643217, "8"],
                [434670, "0"],
                [502110, "7"],
                [519048, "3"],
                [646240, "5"],
                [543877, "2"],
                [571788, "4"],
                [624407, "6"],
            ],
            "bench": [
                [456488, "SS"],
                [596119, "C"],
                [605141, "SS"],
                [506702, "C"],
            ],
            "bullpen": [
                593958,
                605476,
                519144,
                598271,
                592390,
                456034,
                518886,
                584171,
                519393,
                523260,
                598264,
            ],
        },
        "umpires": {
            "HP": "Gary Cederstrom",
            "1B": "Eric Cooper",
            "2B": "Cory Blaser",
            "3B": "Stu Scheurwater",
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
# Pitching: BOS #42 Chris Sale
t1 = game.new_inning()

# 1. BAL #42 Trey Mancini (X - X - X)
t1.new_ab()
t1.hit(1)
t1.advance(4, "42 2B")

# 2. BAL #42 Craig Gentry (X - X - 42)
t1.new_ab()
t1.pitch_list("l b b c f f f f 1 c")
t1.out("!K")

# 3. BAL #42 Manny Machado (X - X - 42)
t1.new_ab()
t1.pitch_list("f b b s b")
t1.hit(2, rbis=1)
t1.advance(3, "42 G4-3")

# 4. BAL #42 Adam Jones (X - 42 - X)
t1.new_ab()
t1.out("G4-3")

# 5. BAL #42  Danny Valencia (42 - X - X)
t1.new_ab()
t1.pitch_list("b b c")
t1.out("G6-3")


# Bot 1st
# Pitching: BAL #42 Dylan Bundy
b1 = game.new_inning()

# 1. BOS #42 Jackie Bradley Jr. (X - X - X)
b1.new_ab()
b1.out("F8")

# 2. BOS #42 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("P6")

# 3. BOS #42 Hanley Ramirez (X - X - X)
b1.new_ab()
b1.out("P4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #42 Chris Sale
t2 = game.new_inning()

# 6. BAL #42 Chris Davis (X - X - X)
t2.new_ab()
t2.pitch_list("c b f c")
t2.out("!K")

# 7. BAL #42  Tim Beckham (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("F8")

# 8. BAL #42 Anthony Santander (X - X - X)
t2.new_ab()
t2.pitch_list("c c b f s")
t2.out("K")


# Bot 2nd
# Pitching: BAL #42 Dylan Bundy
b2 = game.new_inning()

# 4. BOS #42 J.D. Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("f f b s")
b2.out("K")

# 5. BOS #42 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(2)

# 6. BOS #42 Rafael Devers (X - 42 - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")

# 7. BOS #42  Christian Vázquez (X - 42 - 42)
b2.new_ab()
b2.pitch_list("c b c f f s")
b2.out("K")

# 8. BOS #42 Brock Holt (X - 42 - 42)
b2.new_ab()
b2.pitch_list("f f f")
b2.out("(F)P5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #42 Chris Sale
t3 = game.new_inning()

# 9. BAL #42 Caleb Joseph (X - X - X)
t3.new_ab()
t3.pitch_list("b f f b f f s")
t3.out("K")

# 1. BAL #42 Trey Mancini (X - X - X)
t3.new_ab()
t3.pitch_list("b b c")
t3.out("G3")

# 2. BAL #42 Craig Gentry (X - X - X)
t3.new_ab()
t3.pitch_list("b b f b b")
t3.reach("BB")
t3.advance(2, "42 SB")

# 3. BAL #42 Manny Machado (X - X - 42)
t3.new_ab()
t3.pitch_list("c b f b d")
t3.out("P6")


# Bot 3rd
# Pitching: BAL #42 Dylan Bundy
b3 = game.new_inning()

# 9. BOS #42  Tzu-Wei Lin (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("F9")

# 1. BOS #42 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b l s")
b3.out("G4-3")

# 2. BOS #42 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(2)

# 3. BOS #42 Hanley Ramirez (X - 42 - X)
b3.new_ab()
b3.pitch_list("c b s b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #42 Chris Sale
t4 = game.new_inning()

# 4. BAL #42 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("c b s b f f s")
t4.out("K")

# 5. BAL #42  Danny Valencia (X - X - X)
t4.new_ab()
t4.pitch_list("b c b c b b")
t4.reach("BB")

# 6. BAL #42 Chris Davis (X - X - 42)
t4.new_ab()
t4.pitch_list("c c b f b b f f c")
t4.out("!K")

# 7. BAL #42  Tim Beckham (X - X - 42)
t4.new_ab()
t4.pitch_list("c f 1 b f t")
t4.out("KT")


# Bot 4th
# Pitching: BAL #42 Dylan Bundy
b4 = game.new_inning()

# 4. BOS #42 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b f b b s b")
b4.reach("BB")
b4.advance(2, "42 WP")

# 5. BOS #42 Mitch Moreland (X - X - 42)
b4.new_ab()
b4.out("(F)P5")

# 6. BOS #42 Rafael Devers (X - X - 42)
b4.new_ab()
b4.pitch_list("s 1 b f s")
b4.out("K")

# 7. BOS #42  Christian Vázquez (X - X - 42)
b4.new_ab()
b4.pitch_list("b f f b")
b4.wp()
b4.out("P4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #42 Chris Sale
t5 = game.new_inning()

# 8. BAL #42 Anthony Santander (X - X - X)
t5.new_ab()
t5.pitch_list("c s b b b t")
t5.out("KT")

# 9. BAL #42 Caleb Joseph (X - X - X)
t5.new_ab()
t5.pitch_list("s")
t5.out("G5-3")

# 1. BAL #42 Trey Mancini (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("G1-3")


# Bot 5th
# Pitching: BAL #42 Dylan Bundy
b5 = game.new_inning()

# 8. BOS #42 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("b c s f")
b5.out("L3")

# 9. BOS #42  Tzu-Wei Lin (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.hit(1)
b5.thrown_out(2, "42 FC3-6", 2, 605164)

# 1. BOS #42 Jackie Bradley Jr. (X - X - 42)
b5.new_ab()
b5.pitch_list("c f")
b5.reach("FC3-6")
b5.advance(2, "42 SB")
b5.advance(4, "42 3B")

# 2. BOS #42 Andrew Benintendi (X - X - 42)
b5.new_ab()
b5.pitch_list("c 1 b")
b5.hit(3, rbis=1)

# 3. BOS #42 Hanley Ramirez (42 - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #42 Heath Hembree
t6 = game.new_inning()

# Pitching change (BOS): #42 Heath Hembree replaces #41 Chris Sale
t6.pitching_substitution(592390)

# 2. BAL #42 Craig Gentry (X - X - X)
t6.new_ab()
t6.pitch_list("f b f")
t6.hit(1)

# 3. BAL #42 Manny Machado (X - X - 42)
t6.new_ab()
t6.pitch_list("b 1 1 b")
t6.out("P6")

# 4. BAL #42 Adam Jones (X - X - 42)
t6.new_ab()
t6.out("F7")

# 5. BAL #42  Danny Valencia (X - X - 42)
t6.new_ab()
t6.pitch_list("b 1")
t6.out("G5-3")


# Bot 6th
# Pitching: BAL #42 Dylan Bundy
b6 = game.new_inning()

# 4. BOS #42 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("f")
b6.error(5)
b6.reach("E5")
b6.advance(3, "42 2B")
b6.advance("U", "42 WP")

# 5. BOS #42 Mitch Moreland (X - X - 42)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(2)
b6.advance(3, "42 1B")
b6.advance("U", "42 2B")

# 6. BOS #42 Rafael Devers (42 - 42 - X)
b6.new_ab()
b6.pitch_list("b b s l s")
b6.wp()
b6.out("K")

# 7. BOS #42  Christian Vázquez (X - 42 - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")

# 8. BOS #42 Brock Holt (X - 42 - X)
b6.new_ab()
b6.pitch_list("c f")
b6.hit(1)
b6.advance(3, "42 2B")

# 9. BOS #42  Tzu-Wei Lin (42 - X - 42)
b6.new_ab()
b6.pitch_list("b c c")
b6.hit(2, rbis=1)

# Pitching change (BAL): #42 Richard Bleier replaces #42 Dylan Bundy
b6.pitching_substitution(542947)

# 1. BOS #42 Jackie Bradley Jr. (42 - 42 - X)
b6.new_ab()
b6.pitch_list("b c b f")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #42 Heath Hembree
t7 = game.new_inning()

# 6. BAL #42 Chris Davis (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G3-1")

# 7. BAL #42  Tim Beckham (X - X - X)
t7.new_ab()
t7.pitch_list("b f f b b s")
t7.out("K")

# 8. BAL #42 Anthony Santander (X - X - X)
t7.new_ab()
t7.pitch_list("f b b s s")
t7.out("K")


# Bot 7th
# Pitching: BAL #42 Richard Bleier
b7 = game.new_inning()

# 2. BOS #42 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1)
b7.advance(2, "42 SB")
b7.thrown_out(4, "42 7-2", 3, 542947)

# 3. BOS #42 Hanley Ramirez (X - X - 42)
b7.new_ab()
b7.pitch_list("f f c")
b7.out("!K")

# 4. BOS #42 J.D. Martinez (X - X - 42)
b7.new_ab()
b7.pitch_list("s 1 s d b f s")
b7.out("K")

# 5. BOS #42 Mitch Moreland (X - 42 - X)
b7.new_ab()
b7.hit(1)


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #42 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #42 Matt Barnes replaces #42 Heath Hembree
t8.pitching_substitution(598264)

# Offensive change (BAL): Pinch-hitter #42 Chance Sisco replaces #42 Caleb Joseph, batting 9th
t8.offensive_substitution(9, 642082, "PH")

# 9. BAL #42 Chance Sisco (X - X - X)
t8.new_ab()
t8.pitch_list("c f b c")
t8.out("!K")

# 1. BAL #42 Trey Mancini (X - X - X)
t8.new_ab()
t8.pitch_list("b c b c s")
t8.out("K")

# 2. BAL #42 Craig Gentry (X - X - X)
t8.new_ab()
t8.pitch_list("b c f b b b")
t8.reach("BB")

# 3. BAL #42 Manny Machado (X - X - 42)
t8.new_ab()
t8.pitch_list("f 1 c b 1 b 1")
t8.out("F9")


# Bot 8th
# Pitching: BAL #42 Richard Bleier
b8 = game.new_inning()

# Defensive switch (BAL): #42 Chance Sisco moves to C
b8.defensive_switch(642082, "2")

# 6. BOS #42 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("c b b")
b8.hit(1)
b8.thrown_out(2, "42 FC6-4", 1, 542947)

# 7. BOS #42  Christian Vázquez (X - X - 42)
b8.new_ab()
b8.pitch_list("b f b b")
b8.reach("FC6-4")

# 8. BOS #42 Brock Holt (X - X - 42)
b8.new_ab()
b8.out("F8")

# 9. BOS #42  Tzu-Wei Lin (X - X - 42)
b8.new_ab()
b8.pitch_list("1 1 c d")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #42 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #42 Craig Kimbrel replaces #42 Matt Barnes
t9.pitching_substitution(518886)

# 4. BAL #42 Adam Jones (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("L9")

# Offensive change (BAL): Pinch-hitter #42 Pedro Alvarez replaces #42 Danny Valencia, batting 5th
t9.offensive_substitution(5, 476883, "PH")

# 5. BAL #42 Pedro Alvarez (X - X - X)
t9.new_ab()
t9.pitch_list("s b b c b f f c")
t9.out("!K")

# 6. BAL #42 Chris Davis (X - X - X)
t9.new_ab()
t9.pitch_list("b b c s s")
t9.out("K")

# Winning team: BOS
# WP: BOS #42 Heath Hembree
game.winning_pitcher(592390)
# SV: BOS #42 Craig Kimbrel
game.save_pitcher(518886)

# Loser team: BAL
# LP: BAL #42 Dylan Bundy
game.losing_pitcher(605164, is_away_team=True)

# print(game)
game.generate_scorecard()
