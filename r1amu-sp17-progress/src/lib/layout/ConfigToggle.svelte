<script>
    import Cols from "../cell/Cols.svelte";
    import LabelCursor from "../cell/LabelCursor.svelte";
    import SpanLabelText from "../cell/SpanLabelText.svelte";
    import TogglePrimary from "../cell/TogglePrimary.svelte";
    export let checked;
</script>

<Cols class="l0">
    <LabelCursor class="l2">
        <SpanLabelText class=""><slot /></SpanLabelText>
        <TogglePrimary class="l1" bind:checked />
    </LabelCursor>
</Cols>

<style lang="postcss" module>
    .l0 {
    }
    .l1 {
        @apply py-1;
    }
    .l2 {
        @apply justify-between gap-2;
    }
</style>
