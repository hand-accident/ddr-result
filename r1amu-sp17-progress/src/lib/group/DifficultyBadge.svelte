<script>
    let className;
    export { className as class };
    export let kind;
    import DifficultyBadgeBeginner from "$c/DifficultyBadgeBeginner.svelte";
    import DifficultyBadgeBasic from "$c/DifficultyBadgeBasic.svelte";
    import DifficultyBadgeDifficult from "$c/DifficultyBadgeDifficult.svelte";
    import DifficultyBadgeExpert from "$c/DifficultyBadgeExpert.svelte";
    import DifficultyBadgeChallenge from "$c/DifficultyBadgeChallenge.svelte";
</script>

<svelte:component
    this={(() => {
        switch (kind) {
            case 0:
                return DifficultyBadgeBeginner;
            case 1:
                return DifficultyBadgeBasic;
            case 2:
                return DifficultyBadgeDifficult;
            case 3:
                return DifficultyBadgeExpert;
            default:
                return DifficultyBadgeChallenge;
        }
    })()}
    class={className}
>
    <slot />
</svelte:component>
