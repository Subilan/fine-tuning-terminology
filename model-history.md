# Module History

This page shows the translation module training history.

## on 23.10.28

**Description:** The training file includes an `OriginalText` field, along with its `GoodTranslation` and `BadTranslation`. The prompt used in dataset asks GPT to optimize the `BadTranslation` provided, and the completion is set to the `GoodTranslation`.

**Assessment:** *Kind of* notable. There seems to be less complex sentences that are not commonly used in Chinese. Some of the irregular usage in English can be translated correctly, thanks to the good or bad judgement mode. These changes make the result more natural and readable. But results that are perfect to read are rare.

- Job: `ftjob-y1LTuP27Ms0Z794LLiufxQNA`
- Model (*extends*): `ft:gpt-3.5-turbo-0613:personal::8E95sXpG` (23.10.27)
- Model (*result*): `ft:gpt-3.5-turbo-0613:personal::8ETNi3N8`
- Training File: `file-m5aOwtnc2vqugh6uj3bYAsML`
- Trained Tokens: 14064
- Cost: $0.1

## on 23.10.27

**Description:** The training file includes a number of Chinese-English sentence pairs. This training tried to improve the translation quality, giving short, separated sentences and the corresponding translation to GPT.

**Assessment:** Not notable. There are still many English sentences being translated directly to Chinese without modifying structure to fit the grammar and convention, causing weird reading experience.

**Comparing to GPT-4 Scholar:** On the same level, or lower.

- Job: `ftjob-Fhe2x4BSkcSbYWOVeHJw7hnY`
- Model (*extends*): `ft:gpt-3.5-turbo-0613:personal::8DsAygwF` (23.10.26)
- Model (*result*): `ft:gpt-3.5-turbo-0613:personal::8E95sXpG`
- Training File: `file-blDmMfOyVVTRhO9Dd55Y2wxt`
- Trained Tokens: 24558
- Cost: $0.2

## on 23.10.26

**Description:** This training tried to scale up the vocabulary, and at the same time solidate the previous cognition.

**Assessment:** Not notable, but possibly working (in terminology mapping).

- Job: `ftjob-sTy0XoGOAjBGugCzlIU6IlZ9`
- Model (*extends*): `ft:gpt-3.5-turbo-0613:personal::8DpUIZAv` (23.10.25)
- Model (*result*): `ft:gpt-3.5-turbo-0613:personal::8DsAygwF`
- Training File: `file-pxHKrUtAfzSl6nkVE3K8fDzj`
- Trained Tokens: 23868
- Cost: $0.2

## on 23.10.25

**Description:** This is the initial training of the `gpt-3.5-turbo` model. The training file includes some of the psychological terminologies that may be used in literature.

**Assessment:** Not notable. Phrases in training file are not frequently used by the given essay.

- Job: `ftjob-1Ifh6MVvKlcs6c1hijjzKMU7`
- Model (*result*): `ft:gpt-3.5-turbo-0613:personal::8DpUIZAv`
- Training File: `file-C5y6HQocnwIAbPoQS3jfrP9h`
- Trained Tokens: 23121
- Cost: $0.2