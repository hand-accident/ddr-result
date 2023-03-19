<script>
    import { availability, bpmMain, bpmSub, date, score } from "../arith/ChartCardDisplay.svelte";
    import CardsContainer from "../layout/CardsContainer.svelte";
    import ChartCard from "../layout/ChartCard.svelte";
    import item from "../../sp17.json";
    import { Config } from "../arith/Classes.svelte";
    import { process } from "../arith/Process.svelte";

    /** @type {Config}*/
    export let config;
</script>

<CardsContainer>
    {#each process(item, config) as c}
        <ChartCard name={c.name} kind={c.kind}>
            <svelte:fragment slot="score">
                {score(c.highScore, c.isCleared)}
            </svelte:fragment>
            <svelte:fragment slot="bpmMain">
                {bpmMain(c.bpm.main)}
            </svelte:fragment>
            <svelte:fragment slot="bpmSub">
                {bpmSub(c.bpm.sub)}
            </svelte:fragment>
            <svelte:fragment slot="clearDate">
                {date(c.isCleared, c.clearDay)}
            </svelte:fragment>
            <svelte:fragment slot="availability">
                {availability(c.isDeleted, c.isUnlocked)}
            </svelte:fragment>
        </ChartCard>
    {/each}
</CardsContainer>
