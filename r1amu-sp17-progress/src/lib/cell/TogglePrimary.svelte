<script>
    let className;
    export { className as class };
    export let checked;
    export let name = "",
        id = "";
</script>

<input type="checkbox" {name} {id} bind:checked class="c {className}" />
<slot />

<style lang="postcss" module>
    /* toggle toggle-primary */
    .c {
        @apply shrink-0;
        --tglbg: hsl(var(--b1));
        --handleoffset: 1.5rem;
        --handleoffsetcalculator: calc(var(--handleoffset) * -1);
        --togglehandleborder: 0 0;
        @apply h-6 w-12 cursor-pointer appearance-none border border-base-content border-opacity-20 bg-base-content bg-opacity-50 duration-300 ease-in-out rounded-badge;
        transition: background,
            box-shadow var(--animation-input, 0.2s) ease-in-out;
        box-shadow: var(--handleoffsetcalculator) 0 0 2px var(--tglbg) inset,
            0 0 0 2px var(--tglbg) inset, var(--togglehandleborder);
    }
    [dir="rtl"] .c {
        --handleoffsetcalculator: calc(var(--handleoffset) * 1);
    }
    .c:focus-visible {
        outline: 2px solid hsl(var(--bc));
        outline-offset: 2px;
        outline: 2px solid hsl(var(--p));
    }
    .c:checked {
        --handleoffsetcalculator: var(--handleoffset);
        @apply border-opacity-100 bg-opacity-100;
        @apply border-primary;
        @apply border-primary border-opacity-10 bg-primary text-primary-content;
    }
    [dir="rtl"] .c:checked {
        --handleoffsetcalculator: calc(var(--handleoffset) * -1);
    }
</style>
